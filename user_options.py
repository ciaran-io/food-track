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
                
