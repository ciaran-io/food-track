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
