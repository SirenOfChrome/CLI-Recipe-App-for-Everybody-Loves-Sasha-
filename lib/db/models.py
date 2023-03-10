from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///cookbook.db")

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipe'

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)
    total_cook_time = Column(String)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    instructions = Column(String)

    user = relationship('User', backref='recipes')
    ingredients = relationship("Recipe_Ingredient", back_populates="recipe")

    def __repr__(self):
        return f'<Recipe {self.recipe_name}>'


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f'<User {self.user_name}>'

class Recipe_Ingredient(Base):
    __tablename__ = 'recipe_ingredient'

    recipe_id = Column(Integer, ForeignKey('recipe.recipe_id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    quantity = Column(Integer)

    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    recipes = relationship("Recipe_Ingredient", back_populates="ingredient")


# # Get the recipe you want to delete
# madison = session.query(User).filter_by(first_name='Madison').first()
# session.delete(madison)
# session.commit()

