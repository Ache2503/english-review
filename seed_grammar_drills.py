#!/usr/bin/env python3
"""
Seed de Grammar Drills - Ejercicios intensivos de gramática cronometrados
Organizados por tema gramatical y nivel CEFR
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import GrammarDrill

app = create_app()

GRAMMAR_DRILLS = [
    # ============ A1 LEVEL ============
    {
        'title': 'Present Simple - Verb "To Be"',
        'grammar_topic': 'present_simple_to_be',
        'level': 'A1',
        'time_limit_seconds': 180,
        'passing_score': 70.0,
        'instructions': 'Complete the sentences with am, is, or are. You have 3 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'I ___ a student.', 'correct': ['am'], 'explanation': 'Use "am" with "I".'},
            {'type': 'fill_blank', 'sentence': 'She ___ my sister.', 'correct': ['is'], 'explanation': 'Use "is" with he/she/it.'},
            {'type': 'fill_blank', 'sentence': 'They ___ from Mexico.', 'correct': ['are'], 'explanation': 'Use "are" with they/we/you.'},
            {'type': 'fill_blank', 'sentence': 'We ___ happy today.', 'correct': ['are'], 'explanation': 'Use "are" with we.'},
            {'type': 'fill_blank', 'sentence': 'It ___ a beautiful day.', 'correct': ['is'], 'explanation': 'Use "is" with it.'},
            {'type': 'multiple_choice', 'sentence': '___ you a teacher?', 'options': ['Am', 'Is', 'Are'], 'correct': 2, 'explanation': 'Questions with "you" use "Are".'},
            {'type': 'multiple_choice', 'sentence': 'He ___ not tired.', 'options': ['am', 'is', 'are'], 'correct': 1, 'explanation': 'Use "is" with he.'},
            {'type': 'fill_blank', 'sentence': 'The cats ___ hungry.', 'correct': ['are'], 'explanation': 'Plural subjects use "are".'},
            {'type': 'fill_blank', 'sentence': 'My name ___ John.', 'correct': ['is'], 'explanation': '"Name" is singular, use "is".'},
            {'type': 'multiple_choice', 'sentence': '___ she from Spain?', 'options': ['Am', 'Is', 'Are'], 'correct': 1, 'explanation': 'Questions with "she" use "Is".'},
        ]
    },
    {
        'title': 'Present Simple - Regular Verbs',
        'grammar_topic': 'present_simple_regular',
        'level': 'A1',
        'time_limit_seconds': 180,
        'passing_score': 70.0,
        'instructions': 'Complete with the correct form of the verb. You have 3 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'She ___ (work) in a hospital.', 'correct': ['works'], 'explanation': 'Add -s for he/she/it.'},
            {'type': 'fill_blank', 'sentence': 'They ___ (live) in New York.', 'correct': ['live'], 'explanation': 'No -s for they/we/you.'},
            {'type': 'fill_blank', 'sentence': 'He ___ (play) tennis every Sunday.', 'correct': ['plays'], 'explanation': 'Add -s for he.'},
            {'type': 'fill_blank', 'sentence': 'I ___ (like) pizza.', 'correct': ['like'], 'explanation': 'No -s for I.'},
            {'type': 'fill_blank', 'sentence': 'My cat ___ (sleep) a lot.', 'correct': ['sleeps'], 'explanation': 'Add -s for singular subjects.'},
            {'type': 'multiple_choice', 'sentence': 'She ___ TV every evening.', 'options': ['watch', 'watches', 'watching'], 'correct': 1, 'explanation': 'Add -es after -ch for he/she/it.'},
            {'type': 'multiple_choice', 'sentence': 'We ___ to school by bus.', 'options': ['go', 'goes', 'going'], 'correct': 0, 'explanation': 'No -s for we.'},
            {'type': 'fill_blank', 'sentence': 'The sun ___ (rise) in the east.', 'correct': ['rises'], 'explanation': 'General truths use present simple.'},
            {'type': 'fill_blank', 'sentence': 'Dogs ___ (bark) at strangers.', 'correct': ['bark'], 'explanation': 'Plural subjects - no -s.'},
            {'type': 'multiple_choice', 'sentence': 'He ___ coffee every morning.', 'options': ['drink', 'drinks', 'drinking'], 'correct': 1, 'explanation': 'Add -s for he.'},
        ]
    },
    {
        'title': 'Articles: A, An, The',
        'grammar_topic': 'articles',
        'level': 'A1',
        'time_limit_seconds': 180,
        'passing_score': 70.0,
        'instructions': 'Choose the correct article. You have 3 minutes!',
        'questions': [
            {'type': 'multiple_choice', 'sentence': 'I have ___ dog.', 'options': ['a', 'an', 'the'], 'correct': 0, 'explanation': '"A" before consonant sounds.'},
            {'type': 'multiple_choice', 'sentence': 'She is ___ engineer.', 'options': ['a', 'an', 'the'], 'correct': 1, 'explanation': '"An" before vowel sounds.'},
            {'type': 'multiple_choice', 'sentence': '___ sun is very hot today.', 'options': ['A', 'An', 'The'], 'correct': 2, 'explanation': '"The" for unique objects.'},
            {'type': 'multiple_choice', 'sentence': 'I need ___ umbrella.', 'options': ['a', 'an', 'the'], 'correct': 1, 'explanation': '"An" before "u" when it sounds like "uh".'},
            {'type': 'multiple_choice', 'sentence': 'She is ___ honest person.', 'options': ['a', 'an', 'the'], 'correct': 1, 'explanation': '"An" before silent "h".'},
            {'type': 'multiple_choice', 'sentence': 'I saw ___ movie yesterday.', 'options': ['a', 'an', 'the'], 'correct': 0, 'explanation': '"A" for first mention.'},
            {'type': 'multiple_choice', 'sentence': '___ movie was very good.', 'options': ['A', 'An', 'The'], 'correct': 2, 'explanation': '"The" for specific/already mentioned.'},
            {'type': 'multiple_choice', 'sentence': 'He is ___ university student.', 'options': ['a', 'an', 'the'], 'correct': 0, 'explanation': '"A" - "university" sounds like "you".'},
            {'type': 'multiple_choice', 'sentence': 'I love ___ music.', 'options': ['a', 'an', 'the', '-'], 'correct': 3, 'explanation': 'No article with general concepts.'},
            {'type': 'multiple_choice', 'sentence': 'She plays ___ piano.', 'options': ['a', 'an', 'the'], 'correct': 2, 'explanation': '"The" with musical instruments.'},
        ]
    },
    
    # ============ A2 LEVEL ============
    {
        'title': 'Past Simple - Regular Verbs',
        'grammar_topic': 'past_simple_regular',
        'level': 'A2',
        'time_limit_seconds': 180,
        'passing_score': 70.0,
        'instructions': 'Put the verb in past simple. You have 3 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'I ___ (work) yesterday.', 'correct': ['worked'], 'explanation': 'Add -ed for regular verbs.'},
            {'type': 'fill_blank', 'sentence': 'She ___ (study) for the exam.', 'correct': ['studied'], 'explanation': 'Change y to ied.'},
            {'type': 'fill_blank', 'sentence': 'They ___ (play) football last week.', 'correct': ['played'], 'explanation': 'Add -ed.'},
            {'type': 'fill_blank', 'sentence': 'He ___ (stop) the car.', 'correct': ['stopped'], 'explanation': 'Double consonant before -ed.'},
            {'type': 'fill_blank', 'sentence': 'We ___ (live) in London in 2010.', 'correct': ['lived'], 'explanation': 'Just add -d after e.'},
            {'type': 'fill_blank', 'sentence': 'The meeting ___ (start) at 9 AM.', 'correct': ['started'], 'explanation': 'Add -ed.'},
            {'type': 'fill_blank', 'sentence': 'I ___ (visit) my grandmother yesterday.', 'correct': ['visited'], 'explanation': 'Add -ed.'},
            {'type': 'fill_blank', 'sentence': 'She ___ (arrive) late to the party.', 'correct': ['arrived'], 'explanation': 'Just add -d after e.'},
            {'type': 'fill_blank', 'sentence': 'They ___ (finish) the project.', 'correct': ['finished'], 'explanation': 'Add -ed.'},
            {'type': 'fill_blank', 'sentence': 'He ___ (try) to call you.', 'correct': ['tried'], 'explanation': 'Change y to ied.'},
        ]
    },
    {
        'title': 'Past Simple - Irregular Verbs',
        'grammar_topic': 'past_simple_irregular',
        'level': 'A2',
        'time_limit_seconds': 240,
        'passing_score': 70.0,
        'instructions': 'Write the past simple of these irregular verbs. You have 4 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'I ___ (go) to the store.', 'correct': ['went'], 'explanation': 'go → went'},
            {'type': 'fill_blank', 'sentence': 'She ___ (see) a movie.', 'correct': ['saw'], 'explanation': 'see → saw'},
            {'type': 'fill_blank', 'sentence': 'They ___ (eat) dinner at 8.', 'correct': ['ate'], 'explanation': 'eat → ate'},
            {'type': 'fill_blank', 'sentence': 'He ___ (have) a great time.', 'correct': ['had'], 'explanation': 'have → had'},
            {'type': 'fill_blank', 'sentence': 'We ___ (make) a cake.', 'correct': ['made'], 'explanation': 'make → made'},
            {'type': 'fill_blank', 'sentence': 'I ___ (buy) new shoes.', 'correct': ['bought'], 'explanation': 'buy → bought'},
            {'type': 'fill_blank', 'sentence': 'She ___ (take) the bus.', 'correct': ['took'], 'explanation': 'take → took'},
            {'type': 'fill_blank', 'sentence': 'They ___ (come) late.', 'correct': ['came'], 'explanation': 'come → came'},
            {'type': 'fill_blank', 'sentence': 'He ___ (give) me a gift.', 'correct': ['gave'], 'explanation': 'give → gave'},
            {'type': 'fill_blank', 'sentence': 'We ___ (know) the answer.', 'correct': ['knew'], 'explanation': 'know → knew'},
            {'type': 'fill_blank', 'sentence': 'I ___ (think) about you.', 'correct': ['thought'], 'explanation': 'think → thought'},
            {'type': 'fill_blank', 'sentence': 'She ___ (write) a letter.', 'correct': ['wrote'], 'explanation': 'write → wrote'},
        ]
    },
    {
        'title': 'Prepositions of Time',
        'grammar_topic': 'prepositions_time',
        'level': 'A2',
        'time_limit_seconds': 180,
        'passing_score': 70.0,
        'instructions': 'Choose in, on, or at. You have 3 minutes!',
        'questions': [
            {'type': 'multiple_choice', 'sentence': 'I wake up ___ 7 AM.', 'options': ['in', 'on', 'at'], 'correct': 2, 'explanation': '"At" for specific times.'},
            {'type': 'multiple_choice', 'sentence': 'We have a meeting ___ Monday.', 'options': ['in', 'on', 'at'], 'correct': 1, 'explanation': '"On" for days.'},
            {'type': 'multiple_choice', 'sentence': 'They go on vacation ___ August.', 'options': ['in', 'on', 'at'], 'correct': 0, 'explanation': '"In" for months.'},
            {'type': 'multiple_choice', 'sentence': 'The class starts ___ noon.', 'options': ['in', 'on', 'at'], 'correct': 2, 'explanation': '"At" for noon/midnight.'},
            {'type': 'multiple_choice', 'sentence': 'I was born ___ 1990.', 'options': ['in', 'on', 'at'], 'correct': 0, 'explanation': '"In" for years.'},
            {'type': 'multiple_choice', 'sentence': 'She called ___ the morning.', 'options': ['in', 'on', 'at'], 'correct': 0, 'explanation': '"In" for parts of day.'},
            {'type': 'multiple_choice', 'sentence': 'We met ___ Christmas Day.', 'options': ['in', 'on', 'at'], 'correct': 1, 'explanation': '"On" for specific days.'},
            {'type': 'multiple_choice', 'sentence': 'They arrived ___ night.', 'options': ['in', 'on', 'at'], 'correct': 2, 'explanation': '"At" for night.'},
            {'type': 'multiple_choice', 'sentence': 'I\'ll see you ___ two hours.', 'options': ['in', 'on', 'at'], 'correct': 0, 'explanation': '"In" for future time periods.'},
            {'type': 'multiple_choice', 'sentence': 'The store opens ___ weekends.', 'options': ['in', 'on', 'at'], 'correct': 1, 'explanation': '"On" for weekends.'},
        ]
    },
    
    # ============ B1 LEVEL ============
    {
        'title': 'Present Perfect vs Past Simple',
        'grammar_topic': 'present_perfect_vs_past',
        'level': 'B1',
        'time_limit_seconds': 240,
        'passing_score': 70.0,
        'instructions': 'Choose Present Perfect or Past Simple. You have 4 minutes!',
        'questions': [
            {'type': 'multiple_choice', 'sentence': 'I ___ to Paris three times.', 'options': ['have been', 'went', 'was'], 'correct': 0, 'explanation': 'Present Perfect for life experience.'},
            {'type': 'multiple_choice', 'sentence': 'She ___ to Paris last year.', 'options': ['has been', 'went', 'goes'], 'correct': 1, 'explanation': 'Past Simple with specific past time.'},
            {'type': 'multiple_choice', 'sentence': 'I ___ already ___ breakfast.', 'options': ['have/eaten', 'has/ate', 'had/eat'], 'correct': 0, 'explanation': 'Present Perfect with "already".'},
            {'type': 'multiple_choice', 'sentence': 'He ___ here since 2015.', 'options': ['has lived', 'lived', 'lives'], 'correct': 0, 'explanation': 'Present Perfect with "since".'},
            {'type': 'multiple_choice', 'sentence': 'They ___ married in 2010.', 'options': ['have got', 'got', 'get'], 'correct': 1, 'explanation': 'Past Simple with specific year.'},
            {'type': 'multiple_choice', 'sentence': '___ you ever ___ sushi?', 'options': ['Have/tried', 'Did/try', 'Were/trying'], 'correct': 0, 'explanation': 'Present Perfect with "ever".'},
            {'type': 'multiple_choice', 'sentence': 'I ___ him yesterday.', 'options': ['have seen', 'saw', 'see'], 'correct': 1, 'explanation': 'Past Simple with "yesterday".'},
            {'type': 'multiple_choice', 'sentence': 'She ___ just ___ home.', 'options': ['has/arrived', 'had/arrive', 'did/arrived'], 'correct': 0, 'explanation': 'Present Perfect with "just".'},
            {'type': 'multiple_choice', 'sentence': 'We ___ here for two hours.', 'options': ['have been', 'were', 'are'], 'correct': 0, 'explanation': 'Present Perfect with "for".'},
            {'type': 'multiple_choice', 'sentence': 'When ___ you ___ English?', 'options': ['have/started', 'did/start', 'do/start'], 'correct': 1, 'explanation': '"When" usually uses Past Simple.'},
        ]
    },
    {
        'title': 'Conditionals - First and Second',
        'grammar_topic': 'conditionals_1_2',
        'level': 'B1',
        'time_limit_seconds': 240,
        'passing_score': 70.0,
        'instructions': 'Complete the conditional sentences. You have 4 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'If it rains, I ___ (stay) home.', 'correct': ['will stay', "will stay", "'ll stay"], 'explanation': 'First conditional: if + present, will + verb.'},
            {'type': 'fill_blank', 'sentence': 'If I ___ (be) rich, I would travel.', 'correct': ['were', 'was'], 'explanation': 'Second conditional: if + past, would + verb.'},
            {'type': 'multiple_choice', 'sentence': 'If you study hard, you ___ pass.', 'options': ['will', 'would', 'could have'], 'correct': 0, 'explanation': 'First conditional uses "will".'},
            {'type': 'multiple_choice', 'sentence': 'If I had more time, I ___ exercise more.', 'options': ['will', 'would', 'have'], 'correct': 1, 'explanation': 'Second conditional uses "would".'},
            {'type': 'fill_blank', 'sentence': 'She ___ (help) you if you ask her.', 'correct': ['will help', "'ll help"], 'explanation': 'First conditional with "will".'},
            {'type': 'fill_blank', 'sentence': 'If I ___ (know) the answer, I would tell you.', 'correct': ['knew'], 'explanation': 'Second conditional needs past simple.'},
            {'type': 'multiple_choice', 'sentence': 'If I were you, I ___ accept the offer.', 'options': ['will', 'would', 'am'], 'correct': 1, 'explanation': '"If I were you" is second conditional.'},
            {'type': 'multiple_choice', 'sentence': 'If they arrive early, we ___ start the meeting.', 'options': ['can', 'could', 'would'], 'correct': 0, 'explanation': 'First conditional with "can".'},
            {'type': 'fill_blank', 'sentence': 'What ___ you do if you won the lottery?', 'correct': ['would'], 'explanation': 'Second conditional hypothetical.'},
            {'type': 'multiple_choice', 'sentence': 'Unless you hurry, you ___ miss the bus.', 'options': ['will', 'would', 'might have'], 'correct': 0, 'explanation': '"Unless" is like "if not" - first conditional.'},
        ]
    },
    
    # ============ B2 LEVEL ============
    {
        'title': 'Passive Voice',
        'grammar_topic': 'passive_voice',
        'level': 'B2',
        'time_limit_seconds': 300,
        'passing_score': 70.0,
        'instructions': 'Transform to passive or complete passives. You have 5 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'The report ___ (write) by the manager.', 'correct': ['was written', 'is written'], 'explanation': 'Passive: be + past participle.'},
            {'type': 'fill_blank', 'sentence': 'This book ___ (read) by millions.', 'correct': ['has been read', 'is read'], 'explanation': 'Present Perfect or Present passive.'},
            {'type': 'fill_blank', 'sentence': 'The window ___ (break) yesterday.', 'correct': ['was broken'], 'explanation': 'Past passive.'},
            {'type': 'fill_blank', 'sentence': 'The cake ___ (make) by my grandmother.', 'correct': ['was made', 'is made'], 'explanation': 'Passive: be + made.'},
            {'type': 'fill_blank', 'sentence': 'English ___ (speak) in many countries.', 'correct': ['is spoken'], 'explanation': 'Present passive for general facts.'},
            {'type': 'multiple_choice', 'sentence': 'The work ___ by tomorrow.', 'options': ['will be finished', 'will finish', 'is finishing'], 'correct': 0, 'explanation': 'Future passive.'},
            {'type': 'multiple_choice', 'sentence': 'The car ___ when I arrived.', 'options': ['was being repaired', 'was repairing', 'has repaired'], 'correct': 0, 'explanation': 'Past continuous passive.'},
            {'type': 'fill_blank', 'sentence': 'This software ___ (use) by professionals.', 'correct': ['is used'], 'explanation': 'Present passive.'},
            {'type': 'fill_blank', 'sentence': 'The meeting ___ (cancel) due to rain.', 'correct': ['was cancelled', 'has been cancelled', 'was canceled', 'has been canceled'], 'explanation': 'Passive with past participle.'},
            {'type': 'multiple_choice', 'sentence': 'The project ___ by the end of the month.', 'options': ['will have been completed', 'will complete', 'is completing'], 'correct': 0, 'explanation': 'Future perfect passive.'},
        ]
    },
    {
        'title': 'Third Conditional',
        'grammar_topic': 'third_conditional',
        'level': 'B2',
        'time_limit_seconds': 300,
        'passing_score': 70.0,
        'instructions': 'Complete the third conditional sentences. You have 5 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'If I had studied, I ___ (pass) the exam.', 'correct': ['would have passed', "would've passed"], 'explanation': 'Third conditional: had + past participle, would have + past participle.'},
            {'type': 'fill_blank', 'sentence': 'If she ___ (know), she would have told us.', 'correct': ['had known'], 'explanation': 'Past perfect in if-clause.'},
            {'type': 'multiple_choice', 'sentence': 'If they had arrived earlier, they ___ the train.', 'options': ["wouldn't have missed", "didn't miss", "won't miss"], 'correct': 0, 'explanation': '"Would have + past participle" for unreal past.'},
            {'type': 'fill_blank', 'sentence': 'I ___ (go) if you had invited me.', 'correct': ['would have gone', "would've gone"], 'explanation': 'Result clause uses would have.'},
            {'type': 'fill_blank', 'sentence': 'If he ___ (be) careful, he wouldn\'t have fallen.', 'correct': ['had been'], 'explanation': 'Past perfect with "be".'},
            {'type': 'multiple_choice', 'sentence': 'We ___ if the weather had been better.', 'options': ['would have gone out', 'will go out', 'went out'], 'correct': 0, 'explanation': 'Third conditional for unreal past.'},
            {'type': 'fill_blank', 'sentence': 'If you ___ (tell) me, I could have helped.', 'correct': ['had told'], 'explanation': '"Could have" also works in third conditional.'},
            {'type': 'fill_blank', 'sentence': 'She ___ (not / leave) if she had known the truth.', 'correct': ["wouldn't have left", "would not have left"], 'explanation': 'Negative third conditional.'},
            {'type': 'multiple_choice', 'sentence': 'Had I known, I ___ differently.', 'options': ['would have acted', 'acted', 'would act'], 'correct': 0, 'explanation': 'Inversion in third conditional.'},
            {'type': 'fill_blank', 'sentence': 'If only I ___ (listen) to your advice!', 'correct': ['had listened'], 'explanation': '"If only" with past perfect for regrets.'},
        ]
    },
    
    # ============ C1 LEVEL ============
    {
        'title': 'Advanced Inversions',
        'grammar_topic': 'inversions',
        'level': 'C1',
        'time_limit_seconds': 360,
        'passing_score': 70.0,
        'instructions': 'Complete the inverted sentences correctly. You have 6 minutes!',
        'questions': [
            {'type': 'multiple_choice', 'sentence': 'Not only ___ late, but she also forgot the documents.', 'options': ['she was', 'was she', 'she had been'], 'correct': 1, 'explanation': 'Inversion after "Not only".'},
            {'type': 'multiple_choice', 'sentence': 'Rarely ___ such a beautiful sunset.', 'options': ['I have seen', 'have I seen', 'I saw'], 'correct': 1, 'explanation': 'Inversion after "Rarely".'},
            {'type': 'multiple_choice', 'sentence': 'Never ___ such nonsense!', 'options': ['I have heard', 'have I heard', 'I heard'], 'correct': 1, 'explanation': 'Inversion after "Never".'},
            {'type': 'fill_blank', 'sentence': 'Hardly ___ I arrived when it started raining.', 'correct': ['had'], 'explanation': '"Hardly had I" is correct structure.'},
            {'type': 'multiple_choice', 'sentence': 'Only after the meeting ___ the problem.', 'options': ['did we understand', 'we understood', 'we did understand'], 'correct': 0, 'explanation': 'Inversion after "Only after".'},
            {'type': 'fill_blank', 'sentence': 'Under no circumstances ___ you open this door.', 'correct': ['should', 'must'], 'explanation': 'Inversion with modal verbs.'},
            {'type': 'multiple_choice', 'sentence': 'No sooner ___ home than the phone rang.', 'options': ['I had arrived', 'had I arrived', 'I arrived'], 'correct': 1, 'explanation': '"No sooner had I" structure.'},
            {'type': 'fill_blank', 'sentence': 'Little ___ she know what was about to happen.', 'correct': ['did'], 'explanation': '"Little did she know" structure.'},
            {'type': 'multiple_choice', 'sentence': 'So beautiful ___ the painting that everyone admired it.', 'options': ['is', 'was', 'being'], 'correct': 1, 'explanation': 'Inversion after "So + adjective".'},
            {'type': 'multiple_choice', 'sentence': 'Not until later ___ the truth.', 'options': ['I discovered', 'did I discover', 'I did discover'], 'correct': 1, 'explanation': 'Inversion after "Not until".'},
        ]
    },
    {
        'title': 'Mixed Conditionals',
        'grammar_topic': 'mixed_conditionals',
        'level': 'C1',
        'time_limit_seconds': 360,
        'passing_score': 70.0,
        'instructions': 'Complete with mixed conditional forms. You have 6 minutes!',
        'questions': [
            {'type': 'fill_blank', 'sentence': 'If I had studied medicine, I ___ (be) a doctor now.', 'correct': ['would be'], 'explanation': 'Past condition, present result.'},
            {'type': 'fill_blank', 'sentence': 'If she were more careful, she ___ (not / have) that accident.', 'correct': ["wouldn't have had", "would not have had"], 'explanation': 'Present condition, past result.'},
            {'type': 'multiple_choice', 'sentence': 'If I had taken the job, I ___ in London now.', 'options': ['would be living', 'would have lived', 'lived'], 'correct': 0, 'explanation': 'Past condition → present result.'},
            {'type': 'multiple_choice', 'sentence': 'If she spoke Spanish, she ___ the job last year.', 'options': ['would have got', 'would get', 'got'], 'correct': 0, 'explanation': 'Present condition → past result.'},
            {'type': 'fill_blank', 'sentence': 'If he weren\'t so lazy, he ___ (finish) the project on time.', 'correct': ['would have finished'], 'explanation': 'Present trait, past consequence.'},
            {'type': 'fill_blank', 'sentence': 'If they had saved money, they ___ (not / be) in debt now.', 'correct': ["wouldn't be", "would not be"], 'explanation': 'Past action, present state.'},
            {'type': 'multiple_choice', 'sentence': 'If I were you, I ___ that offer yesterday.', 'options': ['would have accepted', 'would accept', 'accepted'], 'correct': 0, 'explanation': 'Permanent state, past action.'},
            {'type': 'fill_blank', 'sentence': 'If she hadn\'t married him, she ___ (be) happier today.', 'correct': ['would be'], 'explanation': 'Past decision, present situation.'},
            {'type': 'multiple_choice', 'sentence': 'We ___ here if we had taken your advice.', 'options': ["wouldn't be", "won't be", "aren't"], 'correct': 0, 'explanation': 'Past condition, current situation.'},
            {'type': 'fill_blank', 'sentence': 'If I had learned to drive, I ___ (not / depend) on buses now.', 'correct': ["wouldn't depend", "would not depend"], 'explanation': 'Past learning, present dependency.'},
        ]
    },
]


def seed_grammar_drills():
    """Crear Grammar Drills"""
    with app.app_context():
        print("="*70)
        print("📝 CREANDO GRAMMAR DRILLS")
        print("="*70)
        
        added = 0
        skipped = 0
        
        for drill_data in GRAMMAR_DRILLS:
            # Verificar si ya existe
            existing = GrammarDrill.query.filter_by(
                grammar_topic=drill_data['grammar_topic'],
                level=drill_data['level']
            ).first()
            
            if existing:
                skipped += 1
                continue
            
            drill = GrammarDrill(
                title=drill_data['title'],
                grammar_topic=drill_data['grammar_topic'],
                level=drill_data['level'],
                questions=drill_data['questions'],
                time_limit_seconds=drill_data['time_limit_seconds'],
                passing_score=drill_data['passing_score'],
                instructions=drill_data['instructions'],
                is_active=True
            )
            db.session.add(drill)
            added += 1
        
        db.session.commit()
        
        print(f"✅ Grammar Drills creados: {added}")
        print(f"⏭️  Omitidos (ya existían): {skipped}")
        print(f"\n📊 Por nivel:")
        for level in ['A1', 'A2', 'B1', 'B2', 'C1']:
            count = GrammarDrill.query.filter_by(level=level).count()
            print(f"   {level}: {count}")
        print(f"\n📚 Por tema:")
        from sqlalchemy import func
        topics = db.session.query(GrammarDrill.grammar_topic, func.count(GrammarDrill.id)).group_by(GrammarDrill.grammar_topic).all()
        for topic, count in sorted(topics, key=lambda x: x[0]):
            print(f"   {topic}: {count}")
        print("="*70)


if __name__ == '__main__':
    seed_grammar_drills()
