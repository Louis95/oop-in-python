from datetime import  date
from calendar import monthrange
from dateutil.rrule import rrule, MONTHLY


# my_string = '2019-10'

# # Create date object in given time format yyyy-mm-dd
# my_date = datetime.strptime(my_string, "%Y-%m")

# print(my_date)
# fd = monthrange(my_date.year, my_date.month, )
# print(fd[1])

strt_dt = date(2018, 11, 4)
end_dt = date(2019, 11, 4)

dates = [dt for dt in rrule(MONTHLY, dtstart=strt_dt, until=end_dt)]
print(dates)


