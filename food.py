class Food:
    def __init__(self, food='', calories=0, weight=0):
        self.food = food
        self.calories = calories
        self.weight = weight

    def create_food(self) -> list:
        """ Create a new food entry for the day """

        while True:
            message = "\n Add food; Enter your food followed by calories " \
                      "& weight(optional): \n " \
                      "e.g. Cheese, 273, 48 (comma separated) \n "
            data_str = input(message).split(',')
            data_str = [x.lstrip() for x in data_str]  # remove leading spaces

            if len(data_str) < 3:  # Add 0 to values if 2 values are entered
                data_str.append('0')

            if self.validate_data(values=data_str):
                print('Adding new food data..')
                return [self.food, int(self.calories), int(self.weight)]

    def validate_data(self, values) -> bool:
        """ Validate the food data """
        try:
            self.food, self.calories, self.weight = values
            # Check if calories and weight are positive
            if int(self.calories) <= 0 or int(self.weight) < 0:
                raise ValueError(
                    "Calories and weight must be a positive number"
                )

            # check if calories and  are less than 5000
            # and weight less than 1000
            if int(self.calories) > 5000 or int(self.weight) > 1000:
                raise ValueError(
                    "Calories and weight must be less than 5000 and 1000"
                )

            # Check if calories and weight are integers
            elif not self.calories.isdigit() or not self.weight.isdigit():
                raise ValueError("Calories and weight must be a number")

            # Check food is not empty and string
            elif len(self.food) < 1 or self.food.isnumeric() \
                    or len(self.food) > 20:
                raise ValueError(
                    "Food must not be empty and must be a character, \n "
                    "food must be less than 20 characters"
                )
            else:
                return True

        except ValueError as e:
            print(f"\nInvalid input: {e}: \n please try again")
