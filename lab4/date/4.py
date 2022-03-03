from datetime import datetime, time
def seconds(date2, date1):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2022-02-28 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print("seconds:",(seconds(date2, date1)))
