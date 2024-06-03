
class Callme:

    def __init__(self, number=None):
        self.number = number

    def __call__(self, *args, **kwargs):
        print(f'ligue para {self.number if self.number is not None else "sem numero"}')
        return self.number


num = '21976788321'
call = Callme(num)
call()
