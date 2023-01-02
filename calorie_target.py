class CalorieTarget:
    """ A class to represent the calorie target """

    def __init__(self, week, food_week_data, target=0):
        # initialise the class variables
        self.target = target
        self.week = week
        self.food_week_data = food_week_data

    def set_week_target(self):
        """ Set the weekly target """

        while True:
            if self.validate_target():
                break

        # Update the target in the Google sheet if not already set
        if not self.food_week_data.find(str(self.week)):
            self.food_week_data.append_row([self.week, None, self.target])
            print(f"Target set to {self.target}")

        else:
            data_string = input("Target already set. Update? (y/n): ")

            # validate input is y or n keep in loop until valid input
            while data_string.lower() not in ('y', 'n'):
                data_string = input("Please enter y to update or n to cancel: ")

            if data_string == 'y':
                CalorieTarget.update_week_target(self)
            elif data_string == 'n':
                print("Target not updated")

    def update_week_target(self):
        """ Update the target by week """

        week_cell = self.food_week_data.find(str(self.week))
        row = week_cell.row
        self.food_week_data.update_cell(row, 3, self.target)
        print(f"Target updated to {self.target}")

    def get_weekly_target(self):
        """ Get the weekly calorie target """

        week_cell = self.food_week_data.find(str(self.week))
        if not week_cell:
            return 0
        else:
            row = week_cell.row
            
        if self.food_week_data.cell(row, 3).value:
            return int(self.food_week_data.cell(row, 3).value)
        else:
            return 0

    def get_daily_target(self):
        """ Get daily calorie target """
        
        print(f"You're weekly target is set to {self.get_weekly_target()}")
        return round(self.get_weekly_target() / 7)

    def validate_target(self):
        """ Validate the target is between 1 and 70000 and is an integer """

        try:
            self.target = int(input("Enter the weekly target: "))
            if self.target < 1 or self.target > 70000:
                raise ValueError("Please enter a number between 1 and 70000")

        except ValueError as e:
            print(f"Invalid input: {e}")
            return False

        return True
