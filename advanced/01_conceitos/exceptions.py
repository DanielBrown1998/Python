class MyError(Exception):
    pass


class OtherError(Exception):
    pass


def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('adicionando notas ao erro!!!')
    raise exception_

try:
    levantar()
except MyError as error:
    print(f"{error.args}")
    print(f"{error.__class__.__name__}\n")
    exception_ = OtherError("Outro erro")
    raise exception_ from error
