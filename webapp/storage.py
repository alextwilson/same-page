import time

class Storage_Of():
    timestamp = 0

    @staticmethod
    def set_timestamp():
        timestamp = int(time.time())
        Storage_Of.timestamp = timestamp

    @staticmethod
    def print_timestamp():
        print(Storage_Of.timestamp)
