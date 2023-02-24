class KeyValueStore:
    def __init__(self):
        self._data = {}

    def set(self, key, value):
        self._data[key] = value

    def get(self, key):
        return self._data.get(key)

store = KeyValueStore()
store.set('name', 'Maria')
store.set('age', 30)

print(store.__dict__)