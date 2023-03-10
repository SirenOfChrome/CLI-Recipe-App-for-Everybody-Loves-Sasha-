import argparse
from .db.models import *


def addUser():
    print("Enter your first name:")
    first_name = input()
    print("Enter your last name:")
    last_name = input()
    print(f"User {first_name} {last_name} successfully added!")
    
