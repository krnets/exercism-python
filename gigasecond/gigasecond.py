from datetime import timedelta

def add(moment):
    gigasecond = 1e9
    return moment + timedelta(seconds=gigasecond)