import time
import datetime as dt
import jdatetime as jd



def convert_gregorian_persian(df,date_col,format_date):

    df['persian_date'] = [jd.date.fromgregorian(date=dt.datetime.strptime(str(i),str(format_date))) for i in df[date_col]]
    df['gregorian_date'] = [dt.datetime.strptime(str(i), str(format_date)) for i in df[date_col]]
    df['gregorian_date'] = [dt.datetime.date(i) for i in df['gregorian_date']]
    df['persian_month'] = [jd.datetime.jmonth_short(i) for i in df['persian_date']]
    df['persian_weekday'] = [jd.datetime.jweekday_short(i) for i in df['persian_date']]

    return df