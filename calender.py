#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import calendar
import pytz
import uuid
import yaml
from datetime import datetime, date

TIMEZONE = pytz.timezone('Asia/Shanghai')
YEAR = datetime.now(TIMEZONE).year


class VEVENT:
    def __init__(self, saturday_date: date, cnt: int, total: int):
        self.saturday_date = saturday_date
        self.cnt = cnt
        self.total = total

    def __str__(self):
        date_str = self.saturday_date.strftime('%Y%m%d')
        uid = uuid.uuid4()

        return """BEGIN:VEVENT
DTSTART;VALUE=DATE:%s
DTEND;VALUE=DATE:%s
DTSTAMP;VALUE=DATE:%s
UID:%s
CLASS:PUBLIC
SUMMARY;LANGUAGE=zh_CN:月末周六(班) 第%d天/共%d天
DESCRIPTION;LANGUAGE=zh_CN:华为月末周六，第%d天/共%d天\\n\\n日历信息: https://github.com/shink/huawei-saturday
SEQUENCE:0
STATUS:CONFIRMED
TRANSP:TRANSPARENT
X-APPLE-SPECIAL-DAY:ALTERNATE-WORKDAY
X-APPLE-UNIVERSAL-ID:b4745336-0bad-482a-9d64-829d9aa04579
END:VEVENT""" % (date_str, date_str, date_str, uid,
                 self.cnt, self.total, self.cnt, self.total)


class VCALENDAR:
    def __init__(self, year: int, vevent_list: list):
        self.year: int = year
        self.vevent_list: list = vevent_list

    def __str__(self):
        return """BEGIN:VCALENDAR
VERSION:2.0
PRODID:icalendar-huawei
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:%d年华为月末周六
X-WR-TIMEZONE:Asia/Shanghai
X-WR-CALDESC:%d年华为月末周六
BEGIN:VTIMEZONE
TZID:Asia/Shanghai
X-LIC-LOCATION:Asia/Shanghai
BEGIN:STANDARD
TZOFFSETFROM:+0800
TZOFFSETTO:+0800
TZNAME:CST
DTSTART:19700101T000000
END:STANDARD
END:VTIMEZONE
%s
END:VCALENDAR""" % (self.year, self.year,
                    '\n'.join([str(vevent) for vevent in self.vevent_list]))


def parse_arguments(arg: str) -> (list[int or str], list[int or str]):
    res_dct = yaml.safe_load(arg)
    return (res_dct.get('months', []), res_dct.get('days', []))


def get_last_saturday(year: int, month: int) -> date:
    (_, last_day) = calendar.monthrange(year, month)
    for day in range(last_day, 0, -1):
        weekday = calendar.weekday(year, month, day)
        if weekday == 5:  # 周六：5，周日：6
            return date(year, month, day)


def get_calender_content(saturday_dct: dict) -> VCALENDAR:
    total = len(saturday_dct)
    vevent_list = [VEVENT(saturday_date, i + 1, total) for i, saturday_date in enumerate(saturday_dct.values())]
    return VCALENDAR(YEAR, vevent_list)


if __name__ == '__main__':
    """
    输入参数内容示例：
    months:
        - 1
        - 3
        - 5
        - 6
        - 7
        - 8
        - 10
        - 12
    days:
        - 01-01
        - 11-01
        - 12-31
    """
    if (len(sys.argv) <= 1):
        print('Invalid arguments')
        exit(1)

    # 解析参数
    (month_list, day_list) = parse_arguments(sys.argv[1])

    # 指定月份的月末周六
    saturday_dct = {}
    for month in range(1, 13):
        if month in set(month_list):
            saturday_dct[int(month)] = get_last_saturday(YEAR, month)

    # 指定月末周六日期
    for day in day_list:
        specific_date = date.fromisoformat("%d-%s" % (YEAR, day))
        saturday_dct[specific_date.month] = specific_date

    # 转换为 ics 内容格式
    content = get_calender_content(saturday_dct)

    print(content)
