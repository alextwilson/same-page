class Storage_Of():
    timestamp = 0

    @staticmethod
    def set_timestamp(new_timestamp):
        Storage_Of.timestamp = new_timestamp

    @staticmethod
    def print_timestamp():
        print(Storage_Of.timestamp)
