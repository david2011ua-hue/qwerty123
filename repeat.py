# import datetime
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())


# from datetime import datetime 
# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())

# import datetime

# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12 , 30, 15)

# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)


# import datetime

# spesific_date = datetime.datetime( 2020, 1, 7, 14, 30, 15)

# print(spesific_date)

# from datetime import datetime

# now = datetime.now()

# day_of_week = now.weekday()

# from datetime import datetime

# now = datetime.now()

# week = now.weekday()

# print(f" Сьогодні: {week}")

# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime


# from datetime import datetime 


# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12 ,0)

# print( datetime1 == datetime2)

# print( datetime1 != datetime2)

# print( datetime1 < datetime2)

# print( datetime1 > datetime2)

# from datetime import timedelta

# delte = timedelta(
#     days= 53,
#     seconds= 27,
#     microseconds= 10,
#     milliseconds = 29000,
#     minutes = 5,
#     hours = 8, 
#     weeks = 2
# )
# print(delte)

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference) 
# print(difference.total_seconds()) 

# from datetime import datetime

# day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = day_2020 - day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())

# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")


# from datetime import datetime


# date = datetime (year=2027, month=12, day=18)

# ordinal_numbers = date.toordinal()

# print(f"Порядковий номер дати {date} становить {ordinal_numbers}")

# from datetime import datetime

# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)


# from datetime import datetime
# now = datetime.now()

# timestamp = datetime.timestamp(now)
# print(timestamp)

# from datetime import datetime

# timestamp = 1617183600

# dt_object = datetime.fromtimestamp(timestamp)

# print(dt_object)

# datetime_object.strftime(format)

# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) 

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only)

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only)  

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only)

# from datetime import datetime
# now = datetime.now()

# formated_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formated_date)

# formated_date_only = now.strftime("%A, %d %B %Y")
# print(formated_date_only)

# formated_time_only = now.strftime("%I:%M %p")
# print(formated_time_only)

# formated_date_only = now.strftime("%d.%m.%Y")
# print(formated_date_only)
# from datetime import datetime

# def string_to_time(time_string):
#     return datetime.strptime(time_string, "%H:%M").time()

# def time_to_string(time):

#     return time.strftime("%H:%M")
# time_string = "9:30"
# converted_time = string_to_time(time_string)

# from datetime import datetime

# date = datetime( year=2023, month=12, day=18)

# ordinal_number = date.toordinal()
# print(f'порядковий намер дати {date}становить {ordinal_number}')

# from datetime import datetime

# now = datetime.now()

# timestamp = datetime.timestamp(now)
# print(timestamp)


# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)
# print(future_date)yelenchukivan12102015@lyceumpetropavlivskyi.in.ua

# from datetime import datetime, timedelta

# seventh_days_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print( seventh_days_2020 - four_weeks_interval) 
# print( seventh_days_2020 + four_weeks_interval) 4
r = 2