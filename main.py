from lib.helpers import *
from lib.db.models import *



def main():
    user_option()
    ingredient_dictionary = build_ingredient_dictionary()
    check_ingredients(ingredient_dictionary)

    
    
if __name__ == '__main__':
    main()
