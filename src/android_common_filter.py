from filter_base import FilterBase

class AndroidCommonFilter(FilterBase):
    LOG_TYPES = (
        {"title": "logcat -v threadtime",
         "pattern": "(\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}.\d{3}).*(\d{3,}).*(\d{3,}) (\D{1}) (\D+): (.*)",
         "idx_log_time": 2,
         "idx_log_tag": 6,
         "idx_log_msg": 7},

        {"title": "logcat -v time",
         "pattern": "(\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}.\d{3}) \D\/(\D+)\( (\d+)\): (.*)",
         "idx_log_time": 2,
         "idx_log_tag": 3,
         "idx_log_msg": 5},

        {"title": "logcat",
         "pattern": "\D\/(\D+)\( (\d+)\): (.*)",
         "idx_log_time": -1,
         "idx_log_tag": 1,
         "idx_log_msg": 3},
    )

    def passThrough(self, input):
        return input

    def parse(self, input):
        return input

