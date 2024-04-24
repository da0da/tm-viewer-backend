def time_to_str(time: int) -> str:
    milliseconds = time % 1000 // 10
    seconds = (time // 1000) % 60
    minutes = (time // 60000) % 60
    hours = time // 3600000

    return "{:02d}:{:02d}:{:02d}.{:02d}".format(hours, minutes, seconds, milliseconds)
