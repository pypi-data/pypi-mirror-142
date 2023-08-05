from os.path import expanduser
from datetime import datetime, timedelta
from time import time


class Tools:
    @classmethod
    def extend_path(cls, path: str):
        return expanduser(path)


class TimePeriod:
    __time_type = dict(year=1, month=2, days=3, hours=4, minutes=5, seconds=6)
    __datetime_format = "%Y:%m:%d:%H:%M:%S"

    @classmethod
    def timestamp_point(cls, time_stamp: float = time(), time_type_offset=2, time_type: str = "hours", res_func=int):
        point = cls.__time_type[time_type]
        now = datetime.fromtimestamp(time_stamp)
        type_s = now.strftime(cls.__datetime_format).split(':')[:point]
        type_time = int(type_s[-1])
        date_string = ":".join(type_s[:-1]) + f":{type_time-type_time%time_type_offset}" + cls.__fill_format(point)
        return res_func(datetime.strptime(date_string, cls.__datetime_format).timestamp())

    @classmethod
    def now_in_period(cls, time_stamp: float, time_type_offset=2, time_type: str = "hours") -> bool:
        check_stamp = time_stamp+timedelta(**{time_type: time_type_offset}).seconds
        return True if check_stamp >= time() else False

    @classmethod
    def __fill_format(cls, point: int):
        return ":00"*(len(cls.__time_type) - point)
