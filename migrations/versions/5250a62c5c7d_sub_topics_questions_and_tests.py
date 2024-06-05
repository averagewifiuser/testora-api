"""sub topics, questions and tests

Revision ID: 5250a62c5c7d
Revises: 0e37def9a1c0
Create Date: 2024-05-27 18:10:33.139957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5250a62c5c7d'
down_revision = '0e37def9a1c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('correct_answer', sa.Text(), nullable=False),
    sa.Column('possible_answers', sa.Text(), nullable=False),
    sa.Column('sub_topic_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.ForeignKeyConstraint(['sub_topic_id'], ['sub_topic.id'], ),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_question_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('correct_answer', sa.Text(), nullable=False),
    sa.Column('possible_answers', sa.Text(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['parent_question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_question')
    op.drop_table('question')
    # ### end Alembic commands ###