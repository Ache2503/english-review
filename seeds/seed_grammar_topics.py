import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import create_app
from app.extensions import db
from app.models import GrammarTopicContent
from seeds.data.grammar_topics_data import grammar_topics

app = create_app()


def seed_grammar_topics():
    with app.app_context():
        created = 0
        updated = 0
        for slug, topic in grammar_topics.items():
            existing = GrammarTopicContent.query.filter_by(slug=slug).first()
            if existing:
                existing.title = topic['title']
                existing.subtitle = topic.get('subtitle')
                existing.icon = topic.get('icon')
                existing.level = topic.get('level')
                existing.category = topic.get('category')
                existing.description = topic.get('description')
                existing.estimated_time = topic.get('estimated_time')
                existing.sections = topic.get('sections')
                existing.tips = topic.get('tips')
                existing.common_mistakes = topic.get('common_mistakes')
                updated += 1
                print(f"  [UPDATED] {slug}")
            else:
                entry = GrammarTopicContent(
                    slug=slug,
                    title=topic['title'],
                    subtitle=topic.get('subtitle'),
                    icon=topic.get('icon'),
                    level=topic.get('level'),
                    category=topic.get('category'),
                    description=topic.get('description'),
                    estimated_time=topic.get('estimated_time'),
                    sections=topic.get('sections'),
                    tips=topic.get('tips'),
                    common_mistakes=topic.get('common_mistakes'),
                )
                db.session.add(entry)
                created += 1
                print(f"  [CREATED] {slug}")

        db.session.commit()
        print(f"\nDone! Created: {created}, Updated: {updated}, Total: {created + updated}")


if __name__ == '__main__':
    seed_grammar_topics()
