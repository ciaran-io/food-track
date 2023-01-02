import datetime as dt

# Dates
today_date = dt.date.today()
current_week = today_date.isocalendar()[1]

# Create dates for the week
monday = today_date - dt.timedelta(days=today_date.weekday())
sunday = monday + dt.timedelta(days=6)
week_dates = [monday, monday + dt.timedelta(days=1),
              monday + dt.timedelta(days=2),
              monday + dt.timedelta(days=3), monday + dt.timedelta(days=4),
              monday + dt.timedelta(days=5), monday + dt.timedelta(days=6)]
