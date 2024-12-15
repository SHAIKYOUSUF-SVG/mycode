class dd:
    def __init__(self,key,value):
        self.d=dict(zip(key,value))
    def __str__(self):
        return str(self.d)
    def get_keys(self):
        return self.d.keys()
    def get_values(self):
        return self.d.values()
    def get_items(self):
        return self.d.items()
    def pop(self,key):
        self.d.pop(key)
    def popitem(self):
        self.d.popitem()

out=dd(('a','b','c'),(10,30,20))

print(out.get_keys())
print(out.get_values())
print(out.get_items())
out.pop('a')
out.popitem()
print(out)