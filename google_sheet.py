import gspread
from google.oauth2.service_account import Credentials
# List of scopes for the API can access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# File name of the credentials
CREDS = Credentials.from_service_account_file("creds.json")
# Create a copy of the credentials with the specified scopes
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
# Authorize the client sheet
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
# Get the instance of the Spreadsheet
SHEET = GSPREAD_CLIENT.open("food_track")

# Access the specific sheet
foods_sheet = SHEET.worksheet("foods")
foods_week_sheet = SHEET.worksheet("food-weekly")
