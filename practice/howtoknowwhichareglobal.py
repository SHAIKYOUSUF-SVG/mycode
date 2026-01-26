def test():
    x=10
    y=20
    print('locals are ',locals())
    print('globals are ',globals())
    print('globals are',globals()['x'])
    print('globals are',globals()['y'])

x=100,2000
y=200
test()
'''output:
locals are  {'x': 10, 'y': 20}
globals are  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.
SourceFileLoader object at 0x000002B2B0F96150>, '__spec__': None, '__annotations__': {}, '__builtins__': 
<module 'builtins' (built-in)>, '__file__': 'C:\\python\\pycharm\\practice\\howtoknowwhichareglobal.py', '__cached__': 
None, 'test': <function test at 0x000002B2B1369080>, 'x': 100, 'y': 200}
globals are (100, 2000)
globals are 200
'''

