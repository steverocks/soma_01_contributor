class TimeChangedException(Exception):
    def __init__(before, after):
        message = "{before} is larger than {after}".format(before=before, after=after)
        super().__init__(message)
