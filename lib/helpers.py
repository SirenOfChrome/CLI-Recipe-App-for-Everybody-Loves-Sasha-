import argparse
from .db.models import *


def addUser():
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Enter your first name:")
    first_name = input()
    print("Enter your last name:")
    last_name = input()
    new_user = User(first_name=first_name, last_name=last_name)
    session.add(new_user)
    session.commit()
    print(f"User {first_name} {last_name} successfully added!")
    return new_user

# def addRecipe(user, instructions): 
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     print("Enter the recipe name: ")
#     recipe_name = input()
#     print("How much time is needed to cook this meal? (prep time included): ")
#     total_cook_time = input()
#     user_id = user.user_id
#     instructions_id = instructions.instructions_id
    
        
    
def addInstructions(): 
    Session = sessionmaker(bind=engine)
    session = Session()
    print("type out the instructions separated by commas")
    instruction_details = input()
    instructions = Instructions(instruction_details = instruction_details)
    session.add(instructions)
    session.commit()
    print("recipe added")