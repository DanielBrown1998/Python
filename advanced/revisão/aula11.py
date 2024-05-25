
class MyOpen:

    def __init__(self, dir, mode, encoding='utf-8'):
        print(type(self).__name__)
        self.dir = dir
        self.mode = mode
        self.encoding = encoding
        self._arquivo = open(self.dir, self.mode, encoding=self.encoding)

    def __enter__(self):
        print('ENTER')
        return self._arquivo

    def __exit__(self, class_, exception_, traceback_):
        self._arquivo.close()
        print('EXIT')
        exception_.add_note('check your context manager')


with MyOpen(r'./arquivo.txt', 'w') as file:
    file.write('Daniel')
    print(file)
