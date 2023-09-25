import datetime
from datetime import timedelta
from datetime import datetime as dt

# везде используем today, чтобы для тестирования просто менять today, а не крутить дату в системе
asia_ekat = datetime.timezone(timedelta(hours=5))
today = dt.now(tz=asia_ekat)

STUDENT_LIST = []
BIRTHDAY_LIST = []
f = open('students.txt', encoding='utf-8')
for i in f.readlines():
    split = i.split()
    STUDENT_LIST.append([split[0], split[1], split[2]])
    BIRTHDAY_LIST.append(split[3].split('/'))
    BIRTHDAY_LIST[-1][0] = int(BIRTHDAY_LIST[-1][0])
    BIRTHDAY_LIST[-1][1] = int(BIRTHDAY_LIST[-1][1])
    BIRTHDAY_LIST[-1][2] = int(BIRTHDAY_LIST[-1][2])
f.close()
