from lib.helpers import *
from lib.db.models import *



def main():
    add_user()
    ingredient_dictionary = build_ingredient_dictionary()
    check_ingredients(ingredient_dictionary)
    
    
if __name__ == '__main__':
    main()
