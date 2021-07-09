#LaSova- Day / WTD(周一到周日)/ 月報 ( 依自然月)/ YTD (2021/1/4 (Week1)起算)四張報表

import datetime

# 週一出上週一至上週日
# 其他出週一至昨天
def weektodate(today):
    # format: today = datetime.datetime.now()
    if today.weekday() == 0:
        start_date = today - datetime.timedelta(days=today.weekday() + 7)
    else:
        start_date = today - datetime.timedelta(days=today.weekday())
    end_date = today - datetime.timedelta(days=1)
    return start_date, end_date

# 上個月初至上個月底
def monthly(today):
    # today = datetime.datetime.now()
    this_month_start = datetime.datetime(today.year, today.month, 1)
    last_month_end = this_month_start - datetime.timedelta(days=1)
    last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)
    return last_month_start, last_month_end

def yeartodate(today):
    # today = datetime.datetime.now()
    this_year_start = datetime.datetime(today.year, 1, 1)
    # 昨天
    end_date = today - datetime.timedelta(days=1)
    # 取得今年YTD第一天
    # 週一回傳0; 週日回傳6
    if this_year_start.weekday() > 3:
        # 至週末只有三天以下，會被算再前年
        this_ytd_start = this_year_start + datetime.timedelta(days=7 - this_year_start.weekday())
    else:
        # 前年的週一算在今年
        this_ytd_start = this_year_start - datetime.timedelta(days=this_year_start.weekday())
    # 如果昨天小於今年第一天則抓取前年YTD第一天
    if end_date < this_ytd_start:
        last_year_start = datetime.datetime(today.year-1, 1, 1)
        if last_year_start.weekday() > 3:
            last_ytd_start = last_year_start + datetime.timedelta(days=7 - last_year_start.weekday())
        else:
            last_ytd_start = last_year_start - datetime.timedelta(days=last_year_start.weekday())
        start_date = last_ytd_start
    else:
        start_date = this_ytd_start
    return start_date, end_date


def lineforline(date):
    # 去年同期
    pass