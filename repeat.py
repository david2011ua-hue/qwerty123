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

from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime
