import itertools


class Todo:
    id_obj = itertools.count()

    def __init__(self, _name, _description):
        self.id = next(Todo.id_obj)
        self.name = _name
        self.description = _description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
