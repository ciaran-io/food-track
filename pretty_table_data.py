from prettytable import PrettyTable

food_options_table = PrettyTable()
food_options_table.field_names = ["option", "description"]

available_options = ["Add new food entry", "View today's foods", "Set weekly calorie target",
                     "View today's calories", "View weekly calories", "Menu", "Quit"]

for option in range(len(available_options)):
    # Add the options to the food option table
    if option == 5:
        food_options_table.add_row(['m', available_options[option]])
    elif option == 6:
        food_options_table.add_row(['q', available_options[option]])
    else:
        food_options_table.add_row([str(option + 1), available_options[option]])

# Align the description column to the left
food_options_table.align["description"] = "l"
