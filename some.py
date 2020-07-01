class Some:
    name = 'Bob'
    mail = 'bob@gmail.com'
    age = 22

    def __getitem__(self, item):
        return self.item


my_dict = {'a': 1, 'b': 25, 'c': 100}
