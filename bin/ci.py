#!/usr/bin/python
# -*- coding: UTF-8 -*-

from datetime import datetime

import os
import pytz
import yaml
import sys

sys.path.append(".")

import hwsat

TIMEZONE = pytz.timezone('Asia/Shanghai')
YEAR = datetime.now(TIMEZONE).year


def read_conf(conf_path: str) -> tuple:
    with open(conf_path, 'r') as f:
        res_dct = yaml.safe_load(f)
        year = res_dct.get('year', YEAR)
        month_list = res_dct.get('months', [])
        day_list = res_dct.get('days', [])
        return year, month_list, day_list


if __name__ == '__main__':
    # 读取配置
    (year, month_list, day_list) = read_conf('config/sat.yml')

    # 生成日历内容
    calender_content = hwsat.get_saturday_calendar(year, month_list, day_list)

    # 保存 GitHub Actions 环境变量
    gh_env_file = os.getenv('GITHUB_ENV')
    with open(gh_env_file, "a") as f:
        f.write(f"CALENDER_YEAR={year}")
        f.write(f"CALENDER_CONTENT={calender_content}")
