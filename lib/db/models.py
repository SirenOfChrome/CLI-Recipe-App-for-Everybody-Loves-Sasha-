from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)
    total_cook_time = Column(String)
    is_vegetarian = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    instructions_id = Column(Integer, ForeignKey('instructions.instruction_id'), nullable=False)

    user = relationship('User', backref='recipes')
    instructions = relationship('Instructions', backref='recipes')
    
    def __repr__(self):
        return f'<Recipe {self.recipe_name}>'

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    
    def __repr__(self):
        return f'<User {self.user_name}>'

class Instructions(Base):
    __tablename__ = 'instructions'

    instruction_id = Column(Integer, primary_key=True)
    instruction_details = Column(String)
    
    def __repr__(self):
        return f'<Instructions {self.instruction_id}>'

class Recipe_Ingredients(Base):
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    quantity = Column(Integer)
    
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipes")

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    recipes = relationship("Recipe_Ingredients", back_populates="ingredient")



