from google_sheet import *
from calorie_target import CalorieTarget
from calories import Calories
from food import Food
from pretty_table_data import create_daily_food_table, \
    create_weekly_food_table, create_remaining_calories_table, food_options_table
from dates import today_date, week_dates, current_week


class UserOptions:
    """User options class"""

    def __init__(self, user_input):
        self.user_input = user_input

    def user_options(self):
        """Check user input and run the relevant function"""

        match self.user_input:
            case '1':
                # Create new food entry in google sheets
                new_food = Food().create_food()
                new_food.insert(0, str(today_date))  # insert today's date at start of list
                foods_sheet.append_row(new_food)
                print('Food data added successfully')

                # Update the weekly calories
                Calories(date=str(today_date), week=current_week, data=foods_week_sheet) \
                    .update_weekly_calories(calories=int(new_food[2]))

            case '2':
                # View daily food overview
                # All cells in foods sheet with today's date
                today_food_data = foods_sheet.findall(str(today_date))

                # Fix food option to offer create food option if no food is found
                if len(today_food_data) == 0:
                    print('No food data for today')
                else:
                    daily_calorie_target = CalorieTarget(current_week,
                                                         foods_week_sheet).get_daily_target()

                    create_daily_food_table(food_data=today_food_data,
                                            foods_sheet=foods_sheet,
                                            target=daily_calorie_target)

            case '3':
                # Set / update weekly calorie target
                CalorieTarget(week=current_week, food_week_data=foods_week_sheet).set_week_target()

            case '4':
                # View today's calories
                today_calories = Calories(date=str(today_date),
                                          week=current_week,
                                          data=foods_sheet).get_total_calories_by_date()

                calorie_target = CalorieTarget(current_week, foods_week_sheet).get_daily_target()

                if today_calories == 0 or None:
                    print('No calorie data for today')
                    print('Please select option 1 add a food entry')
                elif calorie_target == 0 or None:
                    print('No calorie target set for this week')
                    print('Please select option 1 add a food entry')
                else:
                    create_remaining_calories_table(today_calories, calorie_target)

            case '5':
                # View weekly calories
                daily_calorie_target = CalorieTarget(current_week, foods_week_sheet).get_daily_target()

                weekly_calories = Calories(
                    str(today_date),
                    current_week,
                    foods_sheet
                ).get_total_calories_by_range(week_dates)
                create_weekly_food_table(weekly_calories, daily_calorie_target)

            case 'm':
                # Return to main menu
                print(food_options_table)

            case 'q':
                # Quit the program
                print("Closing application, goodbye.")
                exit()

            case _:
                # If no match is found
                print("Invalid option, please choose an option from the menu \n input 'm' to return to the main menu")
