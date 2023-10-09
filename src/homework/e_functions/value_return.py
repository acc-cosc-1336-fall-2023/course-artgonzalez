#
def get_hour(seconds):
    return seconds // 3600 % 24

def get_minutes(seconds):
    minutes = seconds // 60
    return minutes % 60

def get_seconds(seconds):
    s = seconds % 3600
    return s % 60