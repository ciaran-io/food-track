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

# Create a weekly calorie table
weekly_food_table = PrettyTable()
weekly_food_table.field_names = ["Day", "Calories", "Target", "Remaining", "Percentage"]
days = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#  Crate a table of calories for remaining daily calories
remaining_calories_table = PrettyTable()
remaining_calories_table.field_names = ["Calories", "Target", "Remaining", "Percentage"]


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


def create_weekly_food_table(weekly_calories, target):
    """ Create a table of food from a list of food objects """
    print('Creating weekly food table...')

    for day in range(len(weekly_calories)):

        remaining_calories = return_remaining_calories(weekly_calories[day], target)
        percentage = return_percentage(remaining_calories, target)

        # Add the data to the table
        weekly_food_table.add_row(
            [days[day], weekly_calories[day], target, remaining_calories, percentage]
        )
    print(weekly_food_table)
    # Reset the table to prevent duplicate data
    weekly_food_table.clear_rows()


def create_remaining_calories_table(calories, target):
    """ Create a table of remaining calories for a given date range """
    print("Creating today's food table...")

    remaining_calories = return_remaining_calories(calories, target)
    percentage = return_percentage(remaining_calories, target)

    # Add the data to the table
    remaining_calories_table.add_row(
        [calories, target, remaining_calories, percentage]
    )

    print(remaining_calories_table)
    # Reset the table to prevent duplicate data
    remaining_calories_table.clear_rows()

