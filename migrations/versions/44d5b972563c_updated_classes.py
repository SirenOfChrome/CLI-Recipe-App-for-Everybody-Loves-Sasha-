"""updated classes

Revision ID: 44d5b972563c
Revises: 27495fe9e7bc
Create Date: 2023-03-09 20:03:51.894215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44d5b972563c'
down_revision = '27495fe9e7bc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredient')
    op.drop_table('ingredient')
    op.drop_table('instructions')
    op.drop_table('recipe')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('recipe_id', sa.INTEGER(), nullable=False),
    sa.Column('recipe_name', sa.VARCHAR(), nullable=True),
    sa.Column('total_cook_time', sa.VARCHAR(), nullable=True),
    sa.Column('is_vegetarian', sa.VARCHAR(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('instructions_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['instructions_id'], ['instructions.instruction_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('recipe_id')
    )
    op.create_table('instructions',
    sa.Column('instruction_id', sa.INTEGER(), nullable=False),
    sa.Column('instruction_details', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('instruction_id')
    )
    op.create_table('ingredient',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredient',
    sa.Column('recipe_id', sa.INTEGER(), nullable=False),
    sa.Column('ingredient_id', sa.INTEGER(), nullable=False),
    sa.Column('quantity', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.recipe_id'], ),
    sa.PrimaryKeyConstraint('recipe_id', 'ingredient_id')
    )
    # ### end Alembic commands ###
