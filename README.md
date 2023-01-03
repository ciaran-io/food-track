# Food Track

## Food Track is a web terminal application that allows users to track their food intake, food weight & calories. View your daily & weekly calorie intake & set a weekly calorie goal.
<br>

## View the live application here: [food-track](https://food-track.herokuapp.com/)

![Mockup](/docs/mockup.png)

## How to use

### Step 1. Add a new food entry

- Select option 1 from the main menu
- Enter the food name
- Enter the food calories
- Enter the food weight(optional)

### Step 2. View today's food entries

- Select option 2 from the main menu
This will display all the food entries for today if there are any any.

### Step 3. Set a weekly calorie goal

- Select option 3 from the main menu
- Enter the weekly calorie goal

### Step 4. View the current days foods calories & remaining calories for the day

- Select option 4 from the main menu
- This will display the current days foods calories & remaining calories for the day

### Step 5. View the current weeks foods calories & remaining calories for the week

- Select option 5 from the main menu
- This will display the current weeks foods calories & remaining calories for the week

---

## Features

### Existing Features

#### Main Menu using python package: PrettyTable

  - This allows the user to select from the following options:
    - Add a new food entry
    - View today's food entries
    - Set a weekly calorie goal
    - View the current days foods calories & remaining calories for the day
    - View the current weeks foods calories & remaining calories for the week

#### Add a new food entry

  - This allows the user to add a new food entry to the database
  - Validation is in place to ensure that the user enters a food name, calories & weight
  - The user can enter a weight or leave it blank
  - The user can enter a food name with spaces
  - calories & weight are must be numbers

Terminal output

![Add a new food entry](/docs/add-food.png)]

Google sheet update to reflect the new food entry.

![Add food entry google sheet](/docs/g-sheet-foods.png)

#### View today's food entries

Terminal output
![View today's food entries](/docs/view-todays-food.png)

#### Set a weekly calorie goal

  - This allows the user to set/update a weekly calorie goal
  - Validation is in place to ensure that the user enters a weekly calorie goal that is a number

Terminal output
![Set a weekly calorie goal](/docs/update-weekly-calories.png)

Google sheet calorie update to reflect the new weekly calorie goal.
![Set a weekly calorie goal google sheet](/docs/g-sheet-calorie-update.png)

#### View the current days foods calories & remaining calories for the day

  - This allows the user to view the current days foods calories, daily target & remaining calories for the day.

Terminal output

![View the current days foods calories & remaining calories for the day](/docs/view-todays-calories.png)

#### View the current weeks foods calories & remaining calories for the week

  - This allows the user to view the current weeks foods calories, weekly target & remaining calories for the week.

Terminal output

![View the current weeks foods calories & remaining calories for the week](/docs/view-weekly-calories.png)

### Future Features

- Add a delete food entry option by date or date ranges
- Update a food entry by date or date ranges

---
## Data Model

### The data model for this application is as follows:

UserInputClass: This class is used to validate user input & call other methods.
CaloriesClass: This class is used to calculate the calories for the day & update weekly calories.
CalorieTargetClass: This class is used to set/update the weekly calorie goal.

---
## Technologies Used

- [Python](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
---

