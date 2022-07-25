import datetime
"""
datetime 핵심객체 4가지
"""
# date : 날짜 기능만 제공
print(datetime.date.today())
# time : 시간 기능만 제공
print(datetime.time(hour=14, minute=3, second=10, microsecond=100))
# datetime : 날짜 시간 기능 제공
print(datetime.datetime.now())
print(datetime.datetime(year=2022, month=7, day=25,hour=14, minute=3, second=10, microsecond=100))
# timedelta : 시간 차이를 구할 때 객체 ex) 100일 후
print(datetime.timedelta(days=100))
# 오늘로부터 100일 후
print(datetime.date.today() + datetime.timedelta(days=100))
"""
날짜 변환 (str -> datetime) or (datetime -> 
"""
format = '%Y-%m-%d %H:%M:%S'
datetime_str = '2022-7-25 14:26:14'
# strptime(str, format) : str -> datetime 객체 변환
datetime_dt = datetime.datetime.strptime(datetime_str, format)
print(type(datetime_dt))
print(datetime_dt)
# strftime(format) : datetime -> str 변환
datetime_str = datetime_dt.strftime('%Y-%m-%d %H:%M:%S')
print(type(datetime_str))
print(datetime_str)

""" 
변환 문자열 
"""

