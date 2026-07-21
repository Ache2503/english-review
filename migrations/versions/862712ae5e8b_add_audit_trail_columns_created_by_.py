"""add audit trail columns created_by updated_by

Revision ID: 862712ae5e8b
Revises: migrate_content_001
Create Date: 2026-07-16 23:34:07.091759

"""
from alembic import op
import sqlalchemy as sa

revision = '862712ae5e8b'
down_revision = 'migrate_content_001'
branch_labels = None
depends_on = None

TABLES = [
    'achievement_milestones',
    'concept_synonyms',
    'error_tip_contents',
    'grammar_rules',
    'grammar_topic_contents',
    'mini_games',
    'quick_quiz_questions',
    'quizzes',
    'reading_comprehensions',
    'readings',
    'sentence_pattern_contents',
    'speed_typing_content',
    'study_topic_contents',
    'topics',
    'units',
    'vocabulary_categories',
    'writing_error_patterns',
    'writing_practices',
    'writing_tip_contents',
]


def upgrade():
    for table in TABLES:
        with op.batch_alter_table(table, schema=None) as batch_op:
            batch_op.add_column(sa.Column('created_by', sa.Integer(), nullable=True))
            batch_op.add_column(sa.Column('updated_by', sa.Integer(), nullable=True))
            batch_op.create_foreign_key(None, 'users', ['created_by'], ['id'])
            batch_op.create_foreign_key(None, 'users', ['updated_by'], ['id'])


def downgrade():
    for table in TABLES:
        with op.batch_alter_table(table, schema=None) as batch_op:
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.drop_constraint(None, type_='foreignkey')
            batch_op.drop_column('created_by')
            batch_op.drop_column('updated_by')
