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