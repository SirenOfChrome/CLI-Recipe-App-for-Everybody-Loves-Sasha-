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

'''
# TODO: Recipe_Ingredients class 
    - create Recipe_Ingredients class. follow the syntax shown at https://jupyter-tutorial.readthedocs.io/en/stable/data-processing/postgresql/sqlalchemy.html#database-connection
    - refer to ERD diagram ==> './phase-3-ERD.pdf'
# TODO: Ingredients Class 
    - create Recipe_Ingredients class. follow the syntax shown at https://jupyter-tutorial.readthedocs.io/en/stable/data-processing/postgresql/sqlalchemy.html#database-connection
    - refer to ERD diagram ==> './phase-3-ERD.pdf'
'''



recipe1 = Recipe()

