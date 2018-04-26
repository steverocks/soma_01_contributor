from guid.utils import get_timestamp, til_next_millis
from guid.exceptions import TimeChangedException

import time

class Guid(object):
    DATACENTER_ID_BITS = 5
    WORKER_ID_BITS = 5
    SEQUENCE_BITS = 12
    SEQUENCE_LIMIT = (1 << SEQUENCE_BITS) - 1
    TIMESTAMP_SHIFT = DATACENTER_ID_BITS + WORKER_ID_BITS + SEQUENCE_BITS
    WORKER_ID_SHIFT = SEQUENCE_BITS
    DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
        
    SEQUENCE_MASK = (1 << SEQUENCE_BITS) - 1
    WORKER_ID_MASK = (1 << WORKER_ID_BITS) - 1
    DATACENTER_ID_MASK = (1 << DATACENTER_ID_BITS) - 1

    EPOCH = time.mktime((2018, 1, 1, 0, 0, 0, 0, 0, 0))

    def __init__(self, datacenter_id, worker_id, epoch = None):
        self.datacenter_id = datacenter_id & Guid.DATACENTER_ID_MASK
        self.worker_id = worker_id & Guid.WORKER_ID_MASK
        self.last_timestamp = -1
        self.sequence = 0
        self.epoch = epoch if epoch != None else int(Guid.EPOCH * 1000)

    def next(self):
        timestamp = get_timestamp()
        print(timestamp)
        if (timestamp < self.last_timestamp):
            raise TimeChangedException(self.last_timestamp, timestamp)

        if (timestamp == self.last_timestamp):
            self.sequence = self.sequence + 1
            if self.sequence >= Guid.SEQUENCE_LIMIT:
                timestamp = til_next_millis(self.last_iimestamp)

        if (timestamp > self.last_timestamp):
            self.sequence = 0

        self.last_timestamp = timestamp
        timestamp -= self.epoch
         
        guid = (timestamp << Guid.TIMESTAMP_SHIFT) |\
                 (self.datacenter_id << Guid.DATACENTER_ID_SHIFT) |\
                 (self.worker_id<< Guid.WORKER_ID_SHIFT) |\
                 self.sequence

        return guid


if __name__ == '__main__':
    g = Guid(0,0)
    print(g.next());
    print(g.next());
