from pytz import timezone
import datetime

def time_horizon(timestamp):
    time_array = []
    eastern = timezone('US/Eastern')
    dt = datetime.datetime.fromtimestamp(float(timestamp), eastern)
    today = datetime.datetime.now().date()
    timedelta = today - dt.date()
    days = timedelta.days
    if days <= 1:
        time_array.append('Last Day')
    if days <= 7:
        time_array.append('Last Week')
    if days <= 30:
        time_array.append('Last Month')
    if days <= 365:
        time_array.append('Last Year')
    return time_array

def meal_time(timestamp):
    time_array = []
    eastern = timezone('US/Eastern')
    dt = datetime.datetime.fromtimestamp(float(timestamp), eastern)
    time_str = dt.time().strftime('%H')
    time = int(time_str)
    if time >= 3 and time < 12:
        time_array.append('Breakfast')
    elif time >= 12 and time < 15:
        time_array.append('Lunch')
    elif time >= 15 and time < 18:
        time_array.append('Snack')
    elif time >= 18 or time < 3:
        time_array.append('Dinner')
    return time_array
