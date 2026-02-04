"""
Servicio de Análisis Avanzado de Escritura.

Este módulo proporciona detección automática de errores en textos escritos:
- Errores gramaticales
- Errores ortográficos
- Errores de estilo
- Sugerencias de mejora
- Análisis de estructura de oraciones
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

# Importar LanguageTool si está disponible
try:
    import language_tool_python
    LANGUAGE_TOOL_AVAILABLE = True
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


class ErrorType(Enum):
    """Tipos de errores detectados."""
    GRAMMAR = "grammar"
    SPELLING = "spelling"
    PUNCTUATION = "punctuation"
    STYLE = "style"
    VOCABULARY = "vocabulary"
    STRUCTURE = "structure"


@dataclass
class WritingError:
    """Representa un error detectado en el texto."""
    error_type: ErrorType
    message: str
    context: str
    offset: int
    length: int
    suggestions: List[str]
    severity: str  # low, medium, high
    rule_id: str
    original_text: str
    

@dataclass
class WritingFeedback:
    """Feedback completo del análisis de escritura."""
    errors: List[WritingError]
    score: int
    grade: str
    summary: Dict
    improvements: List[str]
    strengths: List[str]
    statistics: Dict


class WritingAnalyzer:
    """Analizador avanzado de escritura en inglés."""
    
    # Patrones comunes de errores para hispanohablantes
    COMMON_SPANISH_ERRORS = {
        r"\bi am agree\b": "Use 'I agree' (not 'I am agree')",
        r"\bthe people is\b": "Use 'people are' (people is plural)",
        r"\bpeoples\b": "Use 'people' (already plural, no 's' needed)",
        r"\binformations?\b": "'Information' is uncountable (no plural)",
        r"\badvices?\b": "'Advice' is uncountable (use 'pieces of advice')",
        r"\bin the last years\b": "Use 'in recent years' or 'in the last few years'",
        r"\bactually\b": "Make sure 'actually' means 'really' (not 'currently')",
        r"\beventually\b": "Check if you mean 'finally' or 'possibly' (common false friend)",
        r"\bsince \d+ years\b": "Use 'for X years' (since + point in time)",
        r"\bfor a long time ago\b": "Use 'a long time ago' (without 'for')",
        r"\bI have \d+ years\b": "Use 'I am X years old' or 'I've been X for X years'",
        r"\bis very\b(?!\s+\w+\s+(?:to|that))": "Consider using stronger adjectives instead of 'very + adjective'",
        r"\bmake a party\b": "Use 'have/throw a party' (not 'make')",
        r"\bdo a mistake\b": "Use 'make a mistake' (not 'do')",
        r"\bopen the light\b": "Use 'turn on the light' (not 'open')",
        r"\bclose the light\b": "Use 'turn off the light' (not 'close')",
    }
    
    # Patrones para mejorar el estilo
    STYLE_IMPROVEMENTS = {
        r"\bvery good\b": ["excellent", "outstanding", "superb"],
        r"\bvery bad\b": ["terrible", "awful", "dreadful"],
        r"\bvery big\b": ["huge", "enormous", "massive"],
        r"\bvery small\b": ["tiny", "minute", "minuscule"],
        r"\bvery happy\b": ["delighted", "thrilled", "ecstatic"],
        r"\bvery sad\b": ["devastated", "heartbroken", "miserable"],
        r"\bvery tired\b": ["exhausted", "worn out", "drained"],
        r"\bvery angry\b": ["furious", "livid", "irate"],
        r"\bvery scared\b": ["terrified", "petrified", "horrified"],
        r"\bvery cold\b": ["freezing", "frigid", "icy"],
        r"\bvery hot\b": ["scorching", "boiling", "sweltering"],
    }
    
    # Conectores por nivel
    CONNECTORS_BY_LEVEL = {
        'basic': ['and', 'but', 'or', 'so', 'because'],
        'intermediate': ['however', 'therefore', 'moreover', 'although', 'nevertheless'],
        'advanced': ['consequently', 'furthermore', 'notwithstanding', 'hence', 'thus']
    }

    def __init__(self):
        self.tool = get_language_tool() if LANGUAGE_TOOL_AVAILABLE else None
    
    def analyze(self, text: str, context: Optional[Dict] = None) -> WritingFeedback:
        """
        Realiza un análisis completo del texto.
        
        Args:
            text: El texto a analizar
            context: Contexto adicional (unit_number, expected_grammar, etc.)
            
        Returns:
            WritingFeedback con el análisis completo
        """
        errors = []
        strengths = []
        improvements = []
        
        # 1. Análisis con LanguageTool
        if self.tool:
            lt_errors = self._analyze_with_language_tool(text)
            errors.extend(lt_errors)
        
        # 2. Detección de errores comunes para hispanohablantes
        spanish_errors = self._detect_spanish_speaker_errors(text)
        errors.extend(spanish_errors)
        
        # 3. Análisis de estilo
        style_suggestions = self._analyze_style(text)
        errors.extend(style_suggestions)
        
        # 4. Análisis de estructura
        structure_feedback = self._analyze_structure(text)
        errors.extend(structure_feedback.get('errors', []))
        strengths.extend(structure_feedback.get('strengths', []))
        improvements.extend(structure_feedback.get('improvements', []))
        
        # 5. Estadísticas del texto
        statistics = self._calculate_statistics(text)
        
        # 6. Evaluar conectores y cohesión
        cohesion = self._analyze_cohesion(text)
        if cohesion['advanced_connectors'] > 0:
            strengths.append(f"Uso de {cohesion['advanced_connectors']} conectores avanzados")
        if cohesion['total_connectors'] == 0 and statistics['sentence_count'] > 2:
            improvements.append("Añade conectores para mejorar la fluidez del texto")
        
        # 7. Calcular puntuación
        score = self._calculate_score(errors, statistics, cohesion)
        grade = self._get_grade(score)
        
        # 8. Resumen
        summary = {
            'total_errors': len(errors),
            'grammar_errors': len([e for e in errors if e.error_type == ErrorType.GRAMMAR]),
            'spelling_errors': len([e for e in errors if e.error_type == ErrorType.SPELLING]),
            'style_suggestions': len([e for e in errors if e.error_type == ErrorType.STYLE]),
            'word_count': statistics['word_count'],
            'sentence_count': statistics['sentence_count'],
        }
        
        return WritingFeedback(
            errors=errors,
            score=score,
            grade=grade,
            summary=summary,
            improvements=improvements,
            strengths=strengths,
            statistics=statistics
        )
    
    def _analyze_with_language_tool(self, text: str) -> List[WritingError]:
        """Analiza el texto con LanguageTool."""
        errors = []
        
        try:
            matches = self.tool.check(text)
            
            for match in matches:
                # Determinar tipo de error
                category = match.category.lower() if match.category else ''
                
                if 'spelling' in category or 'typo' in category:
                    error_type = ErrorType.SPELLING
                elif 'grammar' in category:
                    error_type = ErrorType.GRAMMAR
                elif 'punctuation' in category:
                    error_type = ErrorType.PUNCTUATION
                elif 'style' in category:
                    error_type = ErrorType.STYLE
                else:
                    error_type = ErrorType.GRAMMAR
                
                # Determinar severidad
                if 'spelling' in category:
                    severity = 'medium'
                elif error_type == ErrorType.GRAMMAR:
                    severity = 'high'
                else:
                    severity = 'low'
                
                error = WritingError(
                    error_type=error_type,
                    message=match.message,
                    context=match.context,
                    offset=match.offset,
                    length=match.errorLength,
                    suggestions=match.replacements[:3] if match.replacements else [],
                    severity=severity,
                    rule_id=match.ruleId or '',
                    original_text=text[match.offset:match.offset + match.errorLength] if match.offset < len(text) else ''
                )
                errors.append(error)
                
        except Exception:
            pass
        
        return errors
    
    def _detect_spanish_speaker_errors(self, text: str) -> List[WritingError]:
        """Detecta errores comunes de hispanohablantes."""
        errors = []
        text_lower = text.lower()
        
        for pattern, message in self.COMMON_SPANISH_ERRORS.items():
            matches = list(re.finditer(pattern, text_lower, re.IGNORECASE))
            
            for match in matches:
                error = WritingError(
                    error_type=ErrorType.GRAMMAR,
                    message=f"⚠️ Posible error común: {message}",
                    context=text[max(0, match.start()-20):min(len(text), match.end()+20)],
                    offset=match.start(),
                    length=match.end() - match.start(),
                    suggestions=[],
                    severity='medium',
                    rule_id='SPANISH_SPEAKER_ERROR',
                    original_text=match.group()
                )
                errors.append(error)
        
        return errors
    
    def _analyze_style(self, text: str) -> List[WritingError]:
        """Analiza y sugiere mejoras de estilo."""
        errors = []
        
        for pattern, alternatives in self.STYLE_IMPROVEMENTS.items():
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
            
            for match in matches:
                error = WritingError(
                    error_type=ErrorType.STYLE,
                    message=f"💡 Sugerencia de estilo: En lugar de '{match.group()}', considera usar palabras más precisas",
                    context=text[max(0, match.start()-15):min(len(text), match.end()+15)],
                    offset=match.start(),
                    length=match.end() - match.start(),
                    suggestions=alternatives,
                    severity='low',
                    rule_id='STYLE_IMPROVEMENT',
                    original_text=match.group()
                )
                errors.append(error)
        
        return errors
    
    def _analyze_structure(self, text: str) -> Dict:
        """Analiza la estructura del texto."""
        result = {
            'errors': [],
            'strengths': [],
            'improvements': []
        }
        
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return result
        
        # Verificar variedad en longitud de oraciones
        lengths = [len(s.split()) for s in sentences]
        avg_length = sum(lengths) / len(lengths) if lengths else 0
        
        if avg_length < 5:
            result['improvements'].append("Intenta construir oraciones más desarrolladas (más de 5 palabras)")
        elif avg_length > 25:
            result['improvements'].append("Considera dividir oraciones muy largas para mayor claridad")
        else:
            result['strengths'].append("Buena longitud promedio de oraciones")
        
        # Verificar variedad de inicios
        sentence_starts = [s.split()[0].lower() if s.split() else '' for s in sentences]
        if len(sentence_starts) > 3:
            unique_starts = len(set(sentence_starts))
            if unique_starts < len(sentence_starts) * 0.5:
                result['improvements'].append("Varía los inicios de tus oraciones para mayor fluidez")
            else:
                result['strengths'].append("Buena variedad en los inicios de oraciones")
        
        # Verificar uso de mayúsculas al inicio
        for i, sentence in enumerate(sentences):
            if sentence and sentence[0].islower():
                error = WritingError(
                    error_type=ErrorType.PUNCTUATION,
                    message="Las oraciones deben comenzar con mayúscula",
                    context=sentence[:50],
                    offset=0,
                    length=1,
                    suggestions=[sentence[0].upper()],
                    severity='medium',
                    rule_id='SENTENCE_CASE',
                    original_text=sentence[0]
                )
                result['errors'].append(error)
        
        return result
    
    def _analyze_cohesion(self, text: str) -> Dict:
        """Analiza la cohesión y uso de conectores."""
        text_lower = text.lower()
        
        basic_count = sum(1 for c in self.CONNECTORS_BY_LEVEL['basic'] 
                         if re.search(rf'\b{c}\b', text_lower))
        intermediate_count = sum(1 for c in self.CONNECTORS_BY_LEVEL['intermediate'] 
                                if re.search(rf'\b{c}\b', text_lower))
        advanced_count = sum(1 for c in self.CONNECTORS_BY_LEVEL['advanced'] 
                           if re.search(rf'\b{c}\b', text_lower))
        
        return {
            'basic_connectors': basic_count,
            'intermediate_connectors': intermediate_count,
            'advanced_connectors': advanced_count,
            'total_connectors': basic_count + intermediate_count + advanced_count
        }
    
    def _calculate_statistics(self, text: str) -> Dict:
        """Calcula estadísticas del texto."""
        words = text.split()
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        # Contar palabras únicas
        unique_words = set(word.lower().strip('.,!?";:') for word in words)
        
        # Calcular complejidad léxica
        lexical_diversity = len(unique_words) / len(words) if words else 0
        
        # Longitud promedio de palabras
        avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
        
        return {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'paragraph_count': len(paragraphs),
            'unique_words': len(unique_words),
            'lexical_diversity': round(lexical_diversity, 2),
            'avg_word_length': round(avg_word_length, 1),
            'avg_sentence_length': round(len(words) / len(sentences), 1) if sentences else 0,
            'characters': len(text),
            'characters_no_spaces': len(text.replace(' ', ''))
        }
    
    def _calculate_score(self, errors: List[WritingError], 
                        statistics: Dict, cohesion: Dict) -> int:
        """Calcula la puntuación final."""
        base_score = 100
        
        # Penalización por errores
        for error in errors:
            if error.severity == 'high':
                base_score -= 5
            elif error.severity == 'medium':
                base_score -= 3
            else:
                base_score -= 1
        
        # Bonificación por extensión (si cumple mínimo)
        if statistics['word_count'] >= 50:
            base_score += 5
        if statistics['word_count'] >= 100:
            base_score += 5
        
        # Bonificación por diversidad léxica
        if statistics['lexical_diversity'] > 0.7:
            base_score += 5
        elif statistics['lexical_diversity'] < 0.4:
            base_score -= 5
        
        # Bonificación por uso de conectores
        if cohesion['intermediate_connectors'] > 0:
            base_score += 3
        if cohesion['advanced_connectors'] > 0:
            base_score += 5
        
        return max(0, min(100, base_score))
    
    def _get_grade(self, score: int) -> str:
        """Convierte puntuación a calificación."""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'


def quick_analyze(text: str) -> Dict:
    """
    Análisis rápido del texto para respuestas en tiempo real.
    
    Returns:
        Dict con errores principales y puntuación
    """
    analyzer = WritingAnalyzer()
    feedback = analyzer.analyze(text)
    
    # Formatear para respuesta rápida
    error_messages = []
    for error in feedback.errors[:5]:  # Máximo 5 errores principales
        if error.suggestions:
            msg = f"• {error.message} → Sugerencia: {', '.join(error.suggestions[:2])}"
        else:
            msg = f"• {error.message}"
        error_messages.append(msg)
    
    return {
        'score': feedback.score,
        'grade': feedback.grade,
        'error_count': len(feedback.errors),
        'errors': error_messages,
        'word_count': feedback.statistics['word_count'],
        'strengths': feedback.strengths[:3],
        'improvements': feedback.improvements[:3]
    }


def get_writing_feedback_html(text: str, unit_number: Optional[int] = None) -> str:
    """
    Genera feedback en formato HTML para mostrar en la interfaz.
    """
    analyzer = WritingAnalyzer()
    feedback = analyzer.analyze(text, {'unit_number': unit_number} if unit_number else None)
    
    html_parts = []
    
    # Encabezado con puntuación
    grade_colors = {'A': 'success', 'B': 'info', 'C': 'warning', 'D': 'warning', 'F': 'danger'}
    html_parts.append(f'''
    <div class="writing-feedback">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h5><i class="fas fa-spell-check me-2"></i>Análisis de Escritura</h5>
            <span class="badge bg-{grade_colors.get(feedback.grade, 'secondary')} fs-5">
                {feedback.score}/100 ({feedback.grade})
            </span>
        </div>
    ''')
    
    # Estadísticas
    html_parts.append(f'''
        <div class="row text-center mb-3">
            <div class="col"><small class="text-muted">Palabras</small><br><strong>{feedback.statistics['word_count']}</strong></div>
            <div class="col"><small class="text-muted">Oraciones</small><br><strong>{feedback.statistics['sentence_count']}</strong></div>
            <div class="col"><small class="text-muted">Errores</small><br><strong class="text-danger">{len(feedback.errors)}</strong></div>
        </div>
    ''')
    
    # Fortalezas
    if feedback.strengths:
        html_parts.append('<div class="alert alert-success py-2"><strong>✓ Fortalezas:</strong><ul class="mb-0">')
        for s in feedback.strengths:
            html_parts.append(f'<li>{s}</li>')
        html_parts.append('</ul></div>')
    
    # Errores
    if feedback.errors:
        html_parts.append('<div class="alert alert-warning py-2"><strong>⚠️ Correcciones sugeridas:</strong><ul class="mb-0">')
        for error in feedback.errors[:7]:  # Máximo 7 errores
            if error.suggestions:
                html_parts.append(f'<li><strong>{error.original_text}</strong>: {error.message}<br>'
                                f'<small class="text-success">→ {", ".join(error.suggestions[:2])}</small></li>')
            else:
                html_parts.append(f'<li>{error.message}</li>')
        html_parts.append('</ul></div>')
    
    # Mejoras
    if feedback.improvements:
        html_parts.append('<div class="alert alert-info py-2"><strong>💡 Para mejorar:</strong><ul class="mb-0">')
        for i in feedback.improvements:
            html_parts.append(f'<li>{i}</li>')
        html_parts.append('</ul></div>')
    
    html_parts.append('</div>')
    
    return ''.join(html_parts)
