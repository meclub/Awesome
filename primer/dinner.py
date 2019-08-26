import datetime
import sched
import time

schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    # 在inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    task()


def timing_exe(cmd, inc=60):
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    schedule.run()  # 持续运行，直到计划时间队列变成空为止


def task():
    print('run schedule task')
    cur = datetime.datetime.now()
    print("" + cur.hour)


print('show time after 2 seconds:')
timing_exe(task, 2)
