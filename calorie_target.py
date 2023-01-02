class CalorieTarget:
    """ A class to represent the calorie target """

    def __init__(self, week, food_week_data, target=0):
        # initialise the class variables
        self.target = target
        self.week = week
        self.food_week_data = food_week_data
