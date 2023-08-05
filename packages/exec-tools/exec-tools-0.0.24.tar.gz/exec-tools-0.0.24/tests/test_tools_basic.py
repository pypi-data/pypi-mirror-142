from exectools.tools_basic import *
from time import time
from datetime import datetime, timedelta


if __name__ == '__main__':
    time_type_args = dict(hours=3)
    time_type, = time_type_args
    time_type_offset = time_type_args[time_type]
    print(datetime.now(), time_type, time_type_offset, '\n')
    for _ in range(time_type_offset*2):
        timestamp = time() - timedelta(**{time_type: _}).seconds + 1
        print(datetime.fromtimestamp(timestamp))
        start = time()
        # res = TimePeriod.timestamp_point(timestamp, time_type_offset, time_type)
        res = TimePeriod.now_in_period(timestamp, time_type_offset, time_type)
        end = time()
        print(res, end-start, '\n')
