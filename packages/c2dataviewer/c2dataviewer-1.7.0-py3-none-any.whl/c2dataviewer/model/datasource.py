import enum

class ConnectionState(enum.Enum):
    CONNECTED = 1
    CONNECTING = 2
    DISCONNECTING = 3
    DISCONNECTED = 4
    FAILED_TO_CONNECT = 5

    def __str__(self):
        string_lookup = {
            1 : 'Connected',
            2 : 'Connecting',
            3 : 'Disconnecting',
            4 : 'Disconnected',
            5 : 'Failed to connect'
        }
        
        return string_lookup[int(self.value)]
