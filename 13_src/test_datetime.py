import datetime

dt = datetime.datetime.now()

# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.microsecond)

print('{}/{}/{}'.format(dt.year, dt.month, dt.day))
print('{}:{}:{} {}'.format(dt.hour, dt.minute, dt.second, dt.microsecond))
