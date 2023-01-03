from messages import welcome_message
from pretty_table_data import food_options_table
from user_options import UserOptions

welcome_message()
print(food_options_table)


def main():
    """ Run all program functions """
    while True:
        user_input = input("\nPlease choose an option: ")
        UserOptions(user_input).user_options()


if __name__ == "__main__":
    main()
