from datetime import date, datetime

from dateutil.relativedelta import relativedelta

NOW = datetime.now()

TODAY = date.today()

print(NOW + relativedelta(months=+1))
