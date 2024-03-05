class Bucket:
    # Initialize bucket here
    def __init__(self):
        self.bucket = []

    # get value from bucket
    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    # put value in bucket
    def update(self, key, value):
        found = False
        for (idx,kv) in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[idx] = (key, value)
                found = True

        if not found:
            self.bucket.append((key,value))

    # delete value from bucket
    def remove(self, key):
        for (i, kv) in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class DesignHashMap():
    # Use the constructor below to initialize the
    # hash map based on the keyspace
    def __init__(self, key_space):
        self.key_space = key_space
        self.bucket = [Bucket()] * self.key_space

    def put(self, key, value):
        if key == None or value == None:
            return

        hash_key = key % self.key_space
        self.bucket[hash_key].update(key, value)

    def get(self, key):
        if key == None:
            return -1

        hash_key = key % self.key_space
        if self.bucket[hash_key]:
            return self.bucket[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space
        self.bucket[hash_key].remove(key)
