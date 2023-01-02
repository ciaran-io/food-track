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

# Create a daily food table
food_table = PrettyTable()
food_table.field_names = ["Food", "Calories", "Weight(g)", "Target", "Remaining", "Percentage"]

def create_daily_food_table(food_data, foods_sheet, target):
    """ Create a table of food from a list of food objects """
    print('Creating daily food table...')
    remaining_calories = target

    for food in food_data:
        row = food.row

        # Reduce the remaining calories by the calories of the food
        # if target is 0 then remaining calories will be 0
        if remaining_calories != 0:
            remaining_calories -= int(foods_sheet.cell(row, 3).value)
        else:
            remaining_calories = 0

        percentage = return_percentage(remaining_calories, target)

        # Add the data to the table
        food_table.add_row([foods_sheet.cell(row, 2).value, foods_sheet.cell(row, 3).value,
                            foods_sheet.cell(row, 4).value, target, remaining_calories, percentage])

    print(food_table)
    # Reset the table to prevent duplicate data
    food_table.clear_rows()


