from app import create_app
from app.extensions import db
from app.models import StudyTopicContent
from app.services.study_content import STUDY_TOPICS

app = create_app()

def seed_study_content():
    with app.app_context():
        count = 0
        skipped = 0

        for slug, data in STUDY_TOPICS.items():
            existing = StudyTopicContent.query.filter_by(slug=slug).first()
            if existing:
                print(f"  Skipped (exists): {slug}")
                skipped += 1
                continue

            topic = StudyTopicContent(
                slug=slug,
                title=data['title'],
                icon=data.get('icon'),
                difficulty=data.get('difficulty'),
                estimated_time=data.get('estimated_time'),
                description=data.get('description'),
                theory=data.get('theory'),
                common_mistakes=data.get('common_mistakes'),
                tips=data.get('tips'),
                exercises=data.get('exercises'),
            )
            db.session.add(topic)
            count += 1
            print(f"  Created: {slug} - {data['title']}")

        db.session.commit()
        print(f"\nDone! Created: {count}, Skipped: {skipped}")

if __name__ == '__main__':
    seed_study_content()
