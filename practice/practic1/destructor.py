'''
destructor-used for =deleting/destroying the object,after running desructor
it will not show
'''


class animal:
    def __init__(self,wild,domestic):
        self.wild=wild
        self.domestic=domestic
    def __del__(self):
        print('deleting')
a=animal('lion','dog')