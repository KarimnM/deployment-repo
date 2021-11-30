import datetime


class WeeklyTimeDelta:
    weekday_name_to_weekday_num = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
    weekday_num_to_weekday_name = {value: key for key, value in weekday_name_to_weekday_num.items()}

    class TimeOfDay:
        def __init__(self, hour: int, minute:int):
            assert 0 <= hour < 25
            assert 0 <= minute < 60
            self.hour = hour
            self.minute = minute

        def __lt__(self, other):
            return self.hour < other.hour or \
                   (self.hour == other.hour and self.minute < other.hour)

        def __eq__(self, other):
            return self.hour == other.hour and self.minute == other.minute

        def __str__(self):
            return f"{self.hour}:{self.minute}"

    # strings must be in the format of HH:MM, where the hour is in range [0, 24), and minute in range [0, 60)
    def __init__(self, weekday_name, start_time: datetime.timedelta, end_time: datetime.timedelta):
        assert weekday_name in WeeklyTimeDelta.weekday_name_to_weekday_num
        self.weekday_name = weekday_name
        self.weekday_num = WeeklyTimeDelta.weekday_name_to_weekday_num[self.weekday_name]

        secs_in_a_hour = 3600
        secs_in_a_minute = 60

        start_total_seconds = int(start_time.total_seconds())
        self.start_time = WeeklyTimeDelta.TimeOfDay(start_total_seconds // secs_in_a_hour,
                                                    start_total_seconds % secs_in_a_hour // secs_in_a_minute)

        end_total_seconds = int(end_time.total_seconds())
        self.end_time = WeeklyTimeDelta.TimeOfDay(end_total_seconds // secs_in_a_hour,
                                                    end_total_seconds % secs_in_a_hour // secs_in_a_minute)

        assert self.start_time < self.end_time


if __name__ == '__main__':
    t1 = datetime.timedelta(hours=1, minutes=30)
    t2 = datetime.timedelta(hours=15, minutes=45)
    w = WeeklyTimeDelta('Tuesday', t1, t2)
    print(w.start_time)
    print(w.end_time)

