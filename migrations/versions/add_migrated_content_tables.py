"""add migrated content tables

Revision ID: migrate_content_001
Revises: 885678244c74
Create Date: 2026-07-13
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'migrate_content_001'
down_revision = '885678244c74'
branch_labels = None
depends_on = None


def upgrade():
    # study_topic_contents
    op.create_table(
        'study_topic_contents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('slug', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('icon', sa.String(10)),
        sa.Column('difficulty', sa.String(30)),
        sa.Column('estimated_time', sa.String(20)),
        sa.Column('description', sa.Text()),
        sa.Column('theory', postgresql.JSON()),
        sa.Column('common_mistakes', postgresql.JSON()),
        sa.Column('tips', postgresql.JSON()),
        sa.Column('exercises', postgresql.JSON()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # grammar_topic_contents
    op.create_table(
        'grammar_topic_contents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('slug', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('subtitle', sa.String(300)),
        sa.Column('icon', sa.String(10)),
        sa.Column('level', sa.String(30)),
        sa.Column('category', sa.String(100)),
        sa.Column('description', sa.Text()),
        sa.Column('estimated_time', sa.String(20)),
        sa.Column('sections', postgresql.JSON()),
        sa.Column('tips', postgresql.JSON()),
        sa.Column('common_mistakes', postgresql.JSON()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # sentence_pattern_contents
    op.create_table(
        'sentence_pattern_contents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('topic_name', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('patterns', postgresql.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # writing_error_patterns
    op.create_table(
        'writing_error_patterns',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('pattern_type', sa.String(50), nullable=False, index=True),
        sa.Column('pattern', sa.String(300), nullable=False),
        sa.Column('message', sa.Text()),
        sa.Column('replacements', postgresql.JSON()),
        sa.Column('level', sa.String(20)),
        sa.Column('is_active', sa.Boolean(), server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # writing_tip_contents
    op.create_table(
        'writing_tip_contents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('error_type', sa.String(50), nullable=False, unique=True, index=True),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('tips', postgresql.JSON()),
        sa.Column('examples', postgresql.JSON()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # concept_synonyms
    op.create_table(
        'concept_synonyms',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('concept_key', sa.String(100), nullable=False, unique=True, index=True),
        sa.Column('synonyms', postgresql.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # error_tip_contents
    op.create_table(
        'error_tip_contents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('category', sa.String(50), nullable=False, index=True),
        sa.Column('error_type', sa.String(50), nullable=False, index=True),
        sa.Column('tips', postgresql.JSON(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
        sa.UniqueConstraint('category', 'error_type', name='uq_category_error_type'),
    )

    # achievement_milestones
    op.create_table(
        'achievement_milestones',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('milestone_type', sa.String(30), nullable=False, index=True),
        sa.Column('threshold', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('icon', sa.String(10)),
        sa.Column('is_active', sa.Boolean(), server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )


def downgrade():
    op.drop_table('achievement_milestones')
    op.drop_table('error_tip_contents')
    op.drop_table('concept_synonyms')
    op.drop_table('writing_tip_contents')
    op.drop_table('writing_error_patterns')
    op.drop_table('sentence_pattern_contents')
    op.drop_table('grammar_topic_contents')
    op.drop_table('study_topic_contents')
