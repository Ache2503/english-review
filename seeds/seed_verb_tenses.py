#!/usr/bin/env python3
"""
Seed para tiempos verbales (VerbTense)
Conjugaciones completas para los verbos en la base de datos
"""

from app import create_app, db
from app.models import Verb, VerbTense

# Definición de tiempos verbales para verbos regulares e irregulares
TENSE_TEMPLATES = {
    "present_simple": {
        "description": "Present Simple",
        "regular_suffix": {
            "i": "", "you": "", "he_she_it": "s", "we": "", "they": ""
        }
    },
    "past_simple": {
        "description": "Past Simple",
    },
    "present_continuous": {
        "description": "Present Continuous",
        "aux": {"i": "am", "you": "are", "he_she_it": "is", "we": "are", "they": "are"}
    },
    "past_continuous": {
        "description": "Past Continuous",
        "aux": {"i": "was", "you": "were", "he_she_it": "was", "we": "were", "they": "were"}
    },
    "present_perfect": {
        "description": "Present Perfect",
        "aux": {"i": "have", "you": "have", "he_she_it": "has", "we": "have", "they": "have"}
    },
    "future_simple": {
        "description": "Future Simple (will)",
        "aux": "will"
    }
}

def get_ing_form(infinitive):
    """Obtener la forma -ing de un verbo"""
    if infinitive.endswith('ie'):
        return infinitive[:-2] + 'ying'
    elif infinitive.endswith('e') and not infinitive.endswith('ee'):
        return infinitive[:-1] + 'ing'
    elif len(infinitive) >= 3 and infinitive[-1] not in 'aeiouwy' and infinitive[-2] in 'aeiou' and infinitive[-3] not in 'aeiou':
        # Duplicar consonante final (run -> running, stop -> stopping)
        if infinitive not in ['open', 'listen', 'happen', 'enter', 'offer', 'suffer']:
            return infinitive + infinitive[-1] + 'ing'
    return infinitive + 'ing'

def get_third_person(infinitive):
    """Obtener la forma de tercera persona (he/she/it)"""
    if infinitive.endswith(('s', 'sh', 'ch', 'x', 'z', 'o')):
        return infinitive + 'es'
    elif infinitive.endswith('y') and infinitive[-2] not in 'aeiou':
        return infinitive[:-1] + 'ies'
    return infinitive + 's'

def seed_verb_tenses():
    """Poblar la tabla de tiempos verbales"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("📖 AGREGANDO TIEMPOS VERBALES")
        print("=" * 60)
        
        verbs = Verb.query.all()
        
        if not verbs:
            print("❌ No hay verbos en la base de datos. Ejecuta seed_verbs.py primero.")
            return
        
        added = 0
        skipped = 0
        
        for verb in verbs:
            infinitive = verb.infinitive
            past = verb.past_simple
            past_participle = verb.past_participle
            ing_form = get_ing_form(infinitive)
            third_person = get_third_person(infinitive)
            
            tenses_to_add = [
                # Present Simple
                {
                    "tense_name": "present_simple",
                    "i_form": f"I {infinitive}",
                    "you_form": f"You {infinitive}",
                    "he_she_it_form": f"He/She/It {third_person}",
                    "we_form": f"We {infinitive}",
                    "they_form": f"They {infinitive}",
                    "negative_form": f"don't {infinitive} / doesn't {infinitive}",
                    "question_form": f"Do you {infinitive}? / Does he {infinitive}?",
                    "example_affirmative": f"I {infinitive} every day.",
                    "example_negative": f"I don't {infinitive} on weekends.",
                    "example_question": f"Do you {infinitive}?"
                },
                # Past Simple
                {
                    "tense_name": "past_simple",
                    "i_form": f"I {past}",
                    "you_form": f"You {past}",
                    "he_she_it_form": f"He/She/It {past}",
                    "we_form": f"We {past}",
                    "they_form": f"They {past}",
                    "negative_form": f"didn't {infinitive}",
                    "question_form": f"Did you {infinitive}?",
                    "example_affirmative": f"I {past} yesterday.",
                    "example_negative": f"I didn't {infinitive} yesterday.",
                    "example_question": f"Did you {infinitive} yesterday?"
                },
                # Present Continuous
                {
                    "tense_name": "present_continuous",
                    "i_form": f"I am {ing_form}",
                    "you_form": f"You are {ing_form}",
                    "he_she_it_form": f"He/She/It is {ing_form}",
                    "we_form": f"We are {ing_form}",
                    "they_form": f"They are {ing_form}",
                    "negative_form": f"am not / isn't / aren't {ing_form}",
                    "question_form": f"Are you {ing_form}?",
                    "example_affirmative": f"I am {ing_form} right now.",
                    "example_negative": f"I am not {ing_form} at the moment.",
                    "example_question": f"Are you {ing_form}?"
                },
                # Past Continuous
                {
                    "tense_name": "past_continuous",
                    "i_form": f"I was {ing_form}",
                    "you_form": f"You were {ing_form}",
                    "he_she_it_form": f"He/She/It was {ing_form}",
                    "we_form": f"We were {ing_form}",
                    "they_form": f"They were {ing_form}",
                    "negative_form": f"wasn't / weren't {ing_form}",
                    "question_form": f"Were you {ing_form}?",
                    "example_affirmative": f"I was {ing_form} when you called.",
                    "example_negative": f"I wasn't {ing_form} at that time.",
                    "example_question": f"Were you {ing_form}?"
                },
                # Present Perfect
                {
                    "tense_name": "present_perfect",
                    "i_form": f"I have {past_participle}",
                    "you_form": f"You have {past_participle}",
                    "he_she_it_form": f"He/She/It has {past_participle}",
                    "we_form": f"We have {past_participle}",
                    "they_form": f"They have {past_participle}",
                    "negative_form": f"haven't / hasn't {past_participle}",
                    "question_form": f"Have you {past_participle}?",
                    "example_affirmative": f"I have {past_participle} many times.",
                    "example_negative": f"I haven't {past_participle} yet.",
                    "example_question": f"Have you ever {past_participle}?"
                },
                # Future Simple
                {
                    "tense_name": "future_simple",
                    "i_form": f"I will {infinitive}",
                    "you_form": f"You will {infinitive}",
                    "he_she_it_form": f"He/She/It will {infinitive}",
                    "we_form": f"We will {infinitive}",
                    "they_form": f"They will {infinitive}",
                    "negative_form": f"won't {infinitive}",
                    "question_form": f"Will you {infinitive}?",
                    "example_affirmative": f"I will {infinitive} tomorrow.",
                    "example_negative": f"I won't {infinitive} tomorrow.",
                    "example_question": f"Will you {infinitive}?"
                },
            ]
            
            for tense_data in tenses_to_add:
                # Verificar si ya existe
                existing = VerbTense.query.filter_by(
                    verb_id=verb.id,
                    tense_name=tense_data["tense_name"]
                ).first()
                
                if existing:
                    skipped += 1
                    continue
                
                tense = VerbTense(
                    verb_id=verb.id,
                    **tense_data
                )
                db.session.add(tense)
                added += 1
        
        db.session.commit()
        
        total_verbs = len(verbs)
        print(f"✅ Tiempos verbales agregados: {added}")
        print(f"⏭️  Omitidos (ya existían): {skipped}")
        print(f"📊 Verbos procesados: {total_verbs}")
        print(f"📊 Tiempos por verbo: 6")
        print("=" * 60)

if __name__ == "__main__":
    seed_verb_tenses()
