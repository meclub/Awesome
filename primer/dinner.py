import datetime
import logging
import os
import sched
import time

schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, delay):
    schedule.enter(delay, 0, perform_command, (cmd, delay))
    os.system(cmd)

    cur_time = time.time()
    print_log("perform_command time: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cur_time)))
    print_log("perform_command cmd: " + cmd + ", next task delay: " + str(delay))


def schedule_exe(cmd):
    schedule_time = get_schedule_time()
    # 延迟一天，再执行
    delay = 3600 * 24
    schedule.enterabs(schedule_time, 0, perform_command, (cmd, delay))
    schedule.run()  # 持续运行，直到计划时间队列变成空为止


def get_schedule_time():
    cur_time = time.time()
    cur_date = datetime.datetime.now()
    cur_hour = cur_date.hour
    cur_minute = cur_date.minute
    # 最晚下午4时点餐，否则定时到第二天点餐
    latest_hour = 16
    if cur_hour < latest_hour:
        value = (latest_hour - cur_hour) * 3600 - cur_minute * 60
    else:
        value = (latest_hour - cur_hour + 24) * 3600 - cur_minute * 60
    schedule_time = cur_time + value
    # print_log("schedule_time:" + str(schedule_time))
    print_log("schedule_time: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(schedule_time)))
    return schedule_time


def print_log(msg):
    logger.info(msg)
    print(msg)


def init_log():
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
    logger.setLevel(level=logging.DEBUG)

    # 获取文件日志句柄并设置日志级别，第二层过滤
    handler = logging.FileHandler("dinner.log")
    handler.setLevel(logging.INFO)

    # 生成并设置文件日志格式，其中name为上面设置的mylog
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 获取流句柄并设置日志级别，第二层过滤
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)

    # 为logger对象添加句柄
    logger.addHandler(handler)
    logger.addHandler(console)


# 获取logger对象,取名mylog
logger = logging.getLogger("Dinner")
init_log()

print_log('schedule dinner start !!!')
schedule_exe("source ~/dinner.sh &")
