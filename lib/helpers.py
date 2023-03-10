import argparse
from .db.models import *
from sqlalchemy import func

def add_user():
    Session = sessionmaker(bind=engine)
    session = Session()
    name_tuple = ()
    print("Enter your first name:")
    first_name = input()
    name_tuple += (first_name,)
    print("Enter your last name:")
    last_name = input()
    name_tuple += (last_name,)
    if not user_exists(session, first_name, last_name):
        new_user = User(first_name=first_name, last_name=last_name)
        session.add(new_user)
        session.commit()
        print(f"User {first_name} {last_name} successfully added!")
        recipe = add_recipe(new_user)
        session.add(recipe)
        session.commit()
    else:
        print(f"Welcom back {first_name} {last_name}!")
        
def user_exists(session, first_name, last_name):
    return session.query(User).filter(func.lower(User.first_name) == func.lower(first_name), func.lower(User.last_name) == func.lower(last_name)).first() is not None


def add_recipe(user): 
    print("Enter the recipe name: ")
    recipe_name = input()
    print("How much time is needed to cook this meal? (prep time included): ")
    total_cook_time = input()
    print("enter each of the instructions, separated by ';' for each step")
    instructions = input()
    recipe = Recipe(recipe_name = recipe_name, total_cook_time=total_cook_time, user_id = user.user_id,  instructions=instructions)
    print("recipe added")
    return recipe
        
def build_ingredient_dictionary(): 
    ingredient_dict = {}
    print("Enter an ingredient (singular-case) along with its quantity, separated by a colon (ex: egg:3). When you're finished, type DONE and hit enter.")
    response = input()
    while response != "DONE":
        try:
            ingredient, quantity = response.split(":")
            quantity = int(quantity)
            ingredient_dict[ingredient] = quantity
        except ValueError:
            print(f"Invalid quantity '{quantity}'. Please enter a valid integer.")
        print("Waiting for next entry... (type DONE if finished)") 
        response = input()
    print(ingredient_dict)
    return ingredient_dict

def check_ingredients(ingredient_dict):
    Session = sessionmaker(bind=engine)
    session = Session()
    for ingredient_name in ingredient_dict:
        ingredient = session.query(Ingredient).filter_by(name=ingredient_name).first()
        if ingredient is None:
            # Ingredient doesn't exist in the database, so add it
            ingredient = Ingredient(name=ingredient_name)
            session.add(ingredient)
            session.commit()
            print(f"Added {ingredient_name} to the database!")
        else:
            print(f"fyi, {ingredient_name} already exists in the database")
