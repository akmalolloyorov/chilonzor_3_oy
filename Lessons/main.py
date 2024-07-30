import time

import schedule

count = 0


def print_massage():
    global count
    count += 1
    print(count)


schedule.every(1).second.do(print_massage)

while True:
    schedule.run_pending()
    time.sleep(1)
