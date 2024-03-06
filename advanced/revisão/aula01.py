class Car:
    def __init__(self, name: str, second_name: str | None = None) -> None:
        self.name = name
        self.second_name = second_name

    def acelerar(self) -> None:
        print(f'{self.name} está acelerando!')


class Camera:
    def __init__(self, name: str, filmando: bool = False) -> None:
        self.name = name
        self.filmando = filmando

    def filmar(self) -> None:
        if self.filmando:
            print(f'{self.name} já está filmando...')
            return
        self.filmando = True
        print(f'{self.name} está filmando...')

    def parar_filmar(self) -> None:
        if not self.filmando:
            print(f'{self.name} não está filmando...')
            return
        self.filmando = False
        print(f'{self.name} está parando de filmar...')

    def fotografar(self):
        if self.filmando:
            print(f'Não há como fotografar agora!!!')
            return
        print(f'{self.name} está fotografando!!!')


class Daniel:
    _year = 1998
    _day = 3
    _month = 2  # february
    _name = 'Daniel Brown Rodrigues Mingozzi dos Passos'
    _gender = 'Male'
    _born_date = f"{_month}{_day}{_year}"

    def __init__(self, profissao: str = 'Dev. Fullstack'):
        self.profissao = profissao

    def idade(self):
        import datetime
        year = datetime.datetime.now().year
        today = datetime.datetime.now().day
        month = datetime.datetime.now().month
        print(f"hoje: {today}/{month}/{year}")
        if today != self._day and month < self._month:
            return year - self._year - 1
        return year - self._year



