class Father:
    def __init__(self, name=None, last_name='Passos'):
        self._name_father = name
        self.last_name_father = last_name

    @property
    def name_father(self):
        return self._name_father

    @name_father.setter
    def name_father(self, val):
        self._name_father = val


class Child(Father):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self._last_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, val):
        self._last_name = val


filho = Child("Rafael")
filho.name_father = "Marcelo"
filho.last_name = "Passos"

if filho.last_name != filho.last_name_father:
    print("não são parentes")
else:
    print(filho.name_father, filho.last_name)
