# import required packages and modules
import argparse
from .db.models import *
from sqlalchemy import func

# function to add new user
def add_user():
    
    # create a new session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # initialize an empty tuple to store user's first and last name
    name_tuple = ()
    
    # prompt user to enter first name and add it to name_tuple

    print("\n*** Enter your first name:\n")
    first_name = input()
    print("\n")
    if(first_name == "clear entire db"): 
        clearDatabase()
        return
    name_tuple += (first_name,)
    
    # prompt user to enter last name and add it to name_tuple
    print("*** Enter your last name:")
    print("\n")
    last_name = input()
    print("\n")
    name_tuple += (last_name,)
    
    # check if user exists in the database using the user_exists function
    current_user = user_exists(session, first_name, last_name)
    if not current_user:
        # if user doesn't exist, create a new User object and add it to the database
        current_user = User(first_name=first_name, last_name=last_name)
        session.add(current_user)
        session.commit()
        # print success message and add a recipe for the new user
        print(f"User {first_name} {last_name} successfully added!")
        print("\n")
    else:
        print(f"Welcome back {first_name} {last_name}!")
        print("\n")
        
    recipe = add_recipe(current_user)
    session.add(recipe)
    session.commit()
        
        
# function to check if a user exists in the database
def user_exists(session, first_name, last_name):
    user = session.query(User).filter_by(first_name=first_name, last_name=last_name).first()
    return user

# function to add a recipe for a given user
def add_recipe(user): 
    # prompt user to enter the recipe name
    print("*** Enter the recipe name: ")
    print("\n")
    recipe_name = input()
    print("\n")
    
    # prompt user to enter the total cook time for the recipe (prep time included)
    print("*** How much time is needed to cook this meal? (Write your answer in minutes, prep time included): ")
    print("\n")
    total_cook_time = input()
    print("\n")
    
    # prompt user to enter the instructions for the recipe
    print("*** Enter each of the instructions, separated by ';' for each step")
    print("\n")
    instructions = input()
    print("\n")
    
    # create a new Recipe object and add it to the database
    recipe = Recipe(recipe_name=recipe_name, total_cook_time=total_cook_time, user_id=user.user_id, instructions=instructions)
    print("Recipe added! \n")
    return recipe

# function to build a dictionary of ingredients and their quantities
def build_ingredient_dictionary(): 
    # initialize an empty dictionary to store ingredient names and quantities
    ingredient_dict = {}
    
    # prompt user to enter ingredients and quantities in the format 'ingredient:quantity', separated by a colon
    print("Enter an ingredient (singular-case) along with its quantity, separated by a colon (ex: egg:3). When you're finished, type DONE and hit enter.\n")
    response = input()
    print("\n")
    while response != "DONE":
        try:
            # split user input to extract ingredient and quantity, convert quantity to integer, and add it to the ingredient_dict
            ingredient, quantity = response.split(":")
            quantity = int(quantity)
            ingredient_dict[ingredient] = quantity
        except ValueError:
            print(f"Invalid quantity '{quantity}'. Please enter a valid integer.")
        print("Waiting for next entry... (type DONE if finished)") 
        response = input()
        print("\n")
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
            print(f"{ingredient_name} already exists in the database")

# only use this for dev purposes for quick way to clear db
def clearDatabase(): 
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # delete all rows from each table
    session.query(Ingredient).delete()
    session.query(Recipe).delete()
    session.query(User).delete()

    # commit the changes
    session.commit()