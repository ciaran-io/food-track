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

