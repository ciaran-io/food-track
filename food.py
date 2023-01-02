class Food:
    def __init__(self, food='', calories=0, weight=0):
        self.food = food
        self.calories = calories
        self.weight = weight

    def create_food(self) -> list:
        """ Create a new food entry for the day """

        while True:
            message = "\n Add food; Enter your food followed by calories " \
                      "& weight(optional): \n e.g. Cheese, 273, 48 (comma separated) \n "
            data_str = input(message).split(',')
            data_str = [x.lstrip() for x in data_str]  # remove leading spaces

            if len(data_str) < 3:  # Add 0 to values if 2 values are entered
                data_str.append('0')

            if self.validate_data(values=data_str):
                print('Adding new food data..')
                return [self.food, int(self.calories), int(self.weight)]
