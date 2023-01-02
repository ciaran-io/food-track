class Calories:
    """Calorie  class"""

    def __init__(self, date, week, data):
        # Initialise class variables
        self.date = date
        self.week = week
        self.data = data

    def get_cells_by_date(self) -> list:
        """ Get cells from google sheet by date """
        cell_list = self.data.findall(self.date)
        # print("retrieving foods..")
        return cell_list

    def get_total_calories_by_date(self) -> int:
        """ Get the total calorie amount by date """

        total_weight = 0
        cell_list = self.get_cells_by_date()

        for cell in cell_list:
            row = cell.row
            total_weight += int(self.data.cell(row, 3).value)

        return total_weight

    def get_total_calories_by_range(self, week_dates) -> list:
        """ Get the total calorie amount by date range """

        total_calories = []
        for day in week_dates:
            day = str(day)
            calories = Calories(day, self.week, self.data)
            total_calories.append(calories.get_total_calories_by_date())
        return total_calories

    def update_weekly_calories(self, calories):
        """ Update google sheet weekly calories """

        week_cell = self.data.find(str(self.week))
        if week_cell is None:
            self.data.append_row([self.week, calories])
        else:
            row = week_cell.row
            if self.data.cell(row, 2).value is None:
                self.data.update_cell(row, 2, calories)
            else:
                self.data.update_cell(
                    row, 2, int(self.data.cell(row, 2).value) + calories
                )
