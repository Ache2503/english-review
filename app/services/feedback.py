import re
from typing import Dict, List, Tuple, Optional
import difflib

# Importar LanguageTool para detección de errores
try:
    import language_tool_python
    LANGUAGE_TOOL_AVAILABLE = True
    # Inicializar LanguageTool (singleton)
    _tool = None
    def get_language_tool():
        global _tool
        if _tool is None:
            _tool = language_tool_python.LanguageTool('en-US')
        return _tool
except ImportError:
    LANGUAGE_TOOL_AVAILABLE = False
    def get_language_tool():
        return None

# Simple regex-based analyzers per unit grammar focus

def _match(pattern: str, text: str, flags=re.IGNORECASE) -> bool:
    return re.search(pattern, text, flags) is not None


def _count(pattern: str, text: str, flags=re.IGNORECASE) -> int:
    return len(re.findall(pattern, text, flags))


def check_grammar_errors(text: str) -> Dict:
    """
    Detecta errores gramaticales usando LanguageTool.
    Retorna diccionario con errores y sugerencias.
    """
    if not LANGUAGE_TOOL_AVAILABLE:
        return {"errors": [], "error_count": 0, "available": False}
    
    try:
        tool = get_language_tool()
        matches = tool.check(text)
        
        errors = []
        for match in matches:
            error_info = {
                "message": match.message,
                "context": match.context,
                "offset": match.offset,
                "length": match.errorLength,
                "replacements": match.replacements[:3] if match.replacements else [],
                "rule": match.ruleId,
                "category": match.category
            }
            errors.append(error_info)
        
        return {
            "errors": errors,
            "error_count": len(errors),
            "available": True
        }
    except Exception as e:
        return {"errors": [], "error_count": 0, "available": False, "error": str(e)}


def normalize_answer(text: str) -> str:
    """
    Normaliza una respuesta para comparación flexible.
    - Convierte a minúsculas
    - Elimina puntuación extra
    - Elimina espacios múltiples
    """
    text = text.lower().strip()
    # Eliminar puntuación final
    text = re.sub(r'[.!?]+$', '', text)
    # Normalizar espacios
    text = re.sub(r'\s+', ' ', text)
    # Eliminar comas extras
    text = re.sub(r'\s*,\s*', ' ', text)
    return text


def check_answer_similarity(user_answer: str, correct_answers: List[str], threshold: float = 0.85) -> Tuple[bool, str, float]:
    """
    Verifica si la respuesta del usuario es similar a alguna respuesta correcta.
    Usa difflib para comparación flexible.
    
    Returns:
        (is_correct, matched_answer, similarity_score)
    """
    user_normalized = normalize_answer(user_answer)
    
    best_match = None
    best_score = 0.0
    
    for correct in correct_answers:
        correct_normalized = normalize_answer(correct)
        
        # Comparación exacta (normalizada)
        if user_normalized == correct_normalized:
            return (True, correct, 1.0)
        
        # Comparación por similitud
        similarity = difflib.SequenceMatcher(None, user_normalized, correct_normalized).ratio()
        
        if similarity > best_score:
            best_score = similarity
            best_match = correct
    
    is_correct = best_score >= threshold
    return (is_correct, best_match, best_score)


def analyze_text(text: str, unit_number: int, grammar_titles: Optional[List[str]] = None) -> Dict:
    text = text.strip()
    messages: List[str] = []
    positives = 0
    suggestions = 0
    
    # ===== NUEVO: Análisis con LanguageTool =====
    grammar_check = check_grammar_errors(text)
    
    if grammar_check["available"] and grammar_check["error_count"] > 0:
        error_count = grammar_check["error_count"]
        messages.append(f"⚠️ Se detectaron {error_count} errores gramaticales:")
        
        # Mostrar hasta 5 errores más importantes
        for error in grammar_check["errors"][:5]:
            error_msg = error["message"]
            replacements = error.get("replacements", [])
            
            if replacements:
                suggestions_text = " o ".join([f"'{r}'" for r in replacements[:2]])
                messages.append(f"  • {error_msg} → Sugerencia: {suggestions_text}")
            else:
                messages.append(f"  • {error_msg}")
        
        # Penalizar por errores
        suggestions += min(error_count, 10)  # Máximo 10 penalizaciones
        
        if error_count > 5:
            messages.append("💡 Consejo: Revisa cuidadosamente la concordancia y los tiempos verbales.")
    elif grammar_check["available"]:
        positives += 2
        messages.append("✅ ¡Sin errores gramaticales detectados! Excelente.")
    # ===== FIN NUEVO =====

    # Common general checks
    word_count = len(text.split())
    if word_count < 40:
        suggestions += 1
        messages.append("📝 El texto es corto; intenta desarrollar más ideas (>=40 palabras).")
    elif word_count >= 40:
        positives += 1

    # Helper: decide if a check should run based on grammar_titles
    # Synonyms map for recognizing grammar concepts from various titles
    CONCEPT_SYNONYMS = {}
    try:
        from app.models import ConceptSynonym
        for cs in ConceptSynonym.query.all():
            CONCEPT_SYNONYMS[cs.concept_key] = cs.synonyms or []
    except Exception:
        CONCEPT_SYNONYMS = {
            'articles': ['article', 'articles', 'a/an/the'],
            'used to': ['used to'],
            'passive voice': ['passive voice', 'passive'],
        }

    def has_concept(concept_key: str) -> bool:
        if not grammar_titles:
            return True
        normalized_titles = [t.lower() for t in grammar_titles]
        keywords = CONCEPT_SYNONYMS.get(concept_key, [concept_key])
        return any(any(k in title for k in keywords) for title in normalized_titles)

    # Unit-specific checks
    if unit_number == 7:
        # Used to
        if has_concept('used to'):
            used_to_count = _count(r"\bused to\b", text)
            if used_to_count:
                positives += 1
                messages.append(f"Buen uso de 'used to' ({used_to_count} ocurrencias).")
            else:
                suggestions += 1
                messages.append("Añade una oración con 'used to' para hábitos del pasado.")
        # Articles with 'school'
        if has_concept('articles'):
            if _match(r"\bgo to (the )?school\b", text):
                messages.append("Buen contraste de 'go to school' vs 'go to the school' si el contexto lo requiere.")
        # The overuse heuristic
        if has_concept('articles'):
            the_count = _count(r"\bthe\b", text)
            if the_count > 12:
                suggestions += 1
                messages.append("Revisa el uso de 'the'; podría haber artículos definidos innecesarios.")

    elif unit_number == 8:
        # Reflexive pronouns
        if has_concept('reflexive pronouns'):
            if _match(r"\b(myself|yourself|himself|herself|itself|ourselves|yourselves|themselves)\b", text):
                positives += 1
                messages.append("Se utilizan pronombres reflexivos correctamente.")
            else:
                suggestions += 1
                messages.append("Incluye un pronombre reflexivo (myself, yourself, etc.) cuando el sujeto y objeto coinciden.")
        # Infinitive of purpose
        if has_concept('infinitive of purpose'):
            if _match(r"\b(to)\s+[a-z]+\b", text) and _match(r"\b(go|went|come|came|buy|bought|visit|visited)\b", text):
                positives += 1
                messages.append("Buen uso del infinitivo de propósito (to + verbo).")
            else:
                suggestions += 1
                messages.append("Agrega una frase con 'to + verbo' para indicar propósito.")
        # First conditional
        if has_concept('first conditional'):
            if _match(r"\bIf\b[^.?!]*\b(will|won't)\b", text) or _match(r"\b(will|won't)\b[^.?!]*\bif\b", text):
                positives += 1
                messages.append("Correcto uso del primer condicional (If + Present, Will + Verb).")
            else:
                suggestions += 1
                messages.append("Incluye un primer condicional: 'If + Present, will + base form'.")

    elif unit_number == 9:
        # Second conditional
        if has_concept('second conditional'):
            if _match(r"\bIf\b[^.?!]*\b([a-z]+ed|were)\b[^.?!]*\b(would|wouldn't)\b", text):
                positives += 1
                messages.append("Correcto uso del segundo condicional (If + Past, would + base).")
            else:
                suggestions += 1
                messages.append("Añade un segundo condicional: 'If + Past, would + base'.")
        # Gerunds
        if has_concept('gerunds'):
            if _match(r"\b([A-Z][a-z]+ing|[a-z]+ing)\b", text):
                positives += 1
                messages.append("Incluyes gerundios; verifica su función como sustantivos cuando corresponda.")
            else:
                suggestions += 1
                messages.append("Usa un gerundio como sujeto u objeto (e.g., 'Spending money is easy').")
        # Essential adjective clauses
        if has_concept('adjective clauses'):
            if _match(r"\b(who|which|that)\b", text):
                positives += 1
                messages.append("Buen uso de cláusulas adjetivales esenciales.")
            else:
                suggestions += 1
                messages.append("Incluye una cláusula con 'who/which/that' para definir al sustantivo.")

    elif unit_number == 10:
        # Comparatives
        if has_concept('comparatives'):
            if _match(r"\b(more|less)\s+[a-z]+\s+than\b", text) or _match(r"\b[a-z]+er\s+than\b", text):
                positives += 1
                messages.append("Uso correcto de comparativos (er/more/less ... than).")
            else:
                suggestions += 1
                messages.append("Añade un comparativo (e.g., 'faster than', 'more useful than').")
        # Superlatives
        if has_concept('superlatives'):
            if _match(r"\bthe\s+(most|least)\b", text) or _match(r"\bthe\s+[a-z]+est\b", text):
                positives += 1
                messages.append("Uso correcto de superlativos (the most/least, -est).")
            else:
                suggestions += 1
                messages.append("Incluye un superlativo (e.g., 'the most exciting').")
        # Need to
        if has_concept('need to'):
            if _match(r"\bneed to\b", text):
                positives += 1
                messages.append("Correcto uso de 'need to' para obligación/necessidad.")
            else:
                suggestions += 1
                messages.append("Agrega una oración con 'need to' (obligación/necessidad).")

    elif unit_number == 11:
        # Passive voice
        if has_concept('passive voice'):
            if _match(r"\b(is|are|was|were|been|being)\s+[a-z]+ed\b", text):
                positives += 1
                messages.append("Uso correcto de voz pasiva (be + participio).")
            else:
                suggestions += 1
                messages.append("Incluye una oración en voz pasiva (be + past participle).")
        # Adjective + infinitive
        if has_concept('adjective + infinitive'):
            if _match(r"\b(it\s+is\s+[a-z]+\s+to\s+[a-z]+)\b", text):
                positives += 1
                messages.append("Correcto patrón 'It is [adj] to [verb]'.")
            else:
                suggestions += 1
                messages.append("Usa 'It is [adj] to [verb]' (e.g., 'It is important to...').")
        # -where words
        if has_concept('where words'):
            if _match(r"\b(somewhere|nowhere|everywhere)\b", text):
                positives += 1
                messages.append("Incluyes palabras terminadas en -where (somewhere/nowhere/everywhere).")
            else:
                suggestions += 1
                messages.append("Añade 'somewhere/nowhere/everywhere' cuando corresponda.")

    elif unit_number == 12:
        # Reported speech: detect 'said (that) ...' or 'told ... that'
        if has_concept('reported speech'):
            if _match(r"\b(said|told)\b[^.?!]*\b(that)\b", text):
                positives += 1
                messages.append("Incluyes estilo indirecto (reported speech) con 'said/told that'.")
            else:
                suggestions += 1
                messages.append("Añade reported speech (e.g., 'He said that...').")
        # Past perfect
        if has_concept('past perfect'):
            if _match(r"\bhad\s+[a-z]+ed\b", text):
                positives += 1
                messages.append("Uso correcto del past perfect (had + participio).")
            else:
                suggestions += 1
                messages.append("Incluye una oración con past perfect ('had + past participle').")
        # Should
        if has_concept('should'):
            if _match(r"\bshould\b", text):
                positives += 1
                messages.append("Incluyes recomendaciones con 'should'.")
            else:
                suggestions += 1
                messages.append("Agrega una recomendación con 'should'.")

    # Compute score: baseline 50 + 10 * positives - 5 * suggestions
    score = max(0, min(100, 50 + 10 * positives - 5 * suggestions))

    # Final tips
    if score < 60:
        messages.append("Revisa las reglas clave de la unidad y vuelve a intentar.")
    elif score < 80:
        messages.append("Buen trabajo; puedes mejorar incluyendo más ejemplos de la gramática clave.")
    else:
        messages.append("Excelente; tu texto demuestra dominio de la unidad.")

    return {
        "messages": messages,
        "score": score
    }

def analyze_reading_sentences(sentences: List[str], reading_text: str, unit_number: int) -> Dict:
    """
    Analiza las oraciones extraídas por el usuario de una lectura.
    Verifica:
    - Si están en el texto original
    - Si son oraciones completas
    - Si son relevantes al tema
    """
    messages: List[str] = []
    positives = 0
    suggestions = 0
    
    if not sentences:
        return {"messages": ["Por favor extrae al menos una oración"], "score": 0}
    
    reading_text_lower = reading_text.lower()
    
    # Analizar cada oración
    for idx, sentence in enumerate(sentences, 1):
        sentence = sentence.strip()
        
        if not sentence:
            continue
        
        # Verificar que está en el texto
        if sentence.lower() in reading_text_lower:
            positives += 1
            messages.append(f"✓ Oración {idx}: Correcta - Encontrada en el texto.")
        else:
            # Buscar palabras clave de la oración en el texto
            keywords = sentence.split()[:5]  # Primeras 5 palabras
            if any(kw.lower() in reading_text_lower for kw in keywords if len(kw) > 3):
                positives += 0.5
                messages.append(f"~ Oración {idx}: Similar a texto original pero con cambios.")
            else:
                suggestions += 1
                messages.append(f"✗ Oración {idx}: No encontrada en el texto. Verifica la extracción.")
        
        # Verificar que es oración completa
        if sentence.endswith(('.', '!', '?')):
            positives += 0.5
            messages.append(f"  • Oración {idx}: Puntuación correcta.")
        else:
            messages.append(f"  • Oración {idx}: Agrega puntuación final.")
        
        # Verificar longitud razonable
        word_count = len(sentence.split())
        if 5 <= word_count <= 30:
            positives += 0.5
        else:
            suggestions += 0.5
            messages.append(f"  • Oración {idx}: Puede ser muy corta o muy larga ({word_count} palabras).")
    
    # Calcular puntuación
    total_extracted = len([s for s in sentences if s.strip()])
    base_score = 50
    bonus = (positives / (total_extracted * 2.5)) * 50 if total_extracted > 0 else 0
    penalty = (suggestions / (total_extracted * 2)) * 20 if total_extracted > 0 else 0
    score = max(0, min(100, base_score + bonus - penalty))
    
    # Mensajes adicionales motivacionales
    if score >= 80:
        messages.append("\n✨ Excelente comprensión de lectura. Estás extrayendo información relevante.")
    elif score >= 60:
        messages.append("\n👍 Buen trabajo. Continúa practicando la extracción de información.")
    else:
        messages.append("\n💡 Sugerencia: Lee con más atención y busca oraciones exactas del texto.")
    
    return {
        "messages": messages,
        "score": score
    }