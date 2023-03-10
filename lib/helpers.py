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
    recipe = addRecipe(new_user)
    session.add(recipe)
    session.commit()

def addRecipe(user): 
    print("Enter the recipe name: ")
    recipe_name = input()
    print("How much time is needed to cook this meal? (prep time included): ")
    total_cook_time = input()
    print("enter each of the instructions, separated by ';' for each step")
    instructions = input()
    recipe = Recipe(recipe_name = recipe_name, total_cook_time=total_cook_time, user_id = user.user_id,  instructions=instructions)
    print("recipe added")
    return recipe
        
def addIngredient(): 
    ingredient_list = []
    print("enter in an ingredient along with its quantity, separated by a colon (ex: egg:3)...when you have run out of ingredients, type DONE and hit enter")
    response = input()
    while response != "DONE":
        ingredient_list.append(response)
        print("waiting for next entry...(type DONE if finished)") 
        response = input()
        
        
        
    