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
