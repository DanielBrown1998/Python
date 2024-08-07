
def super_list(*args):
    def union(func):
        def list_intern(*my_args: list | tuple):
            my_list = my_args
            other_list: tuple = func(*args)
            list_final = [(my_list[i], other_list[i]) for i in range(len(my_list))]
            return list_final
        return list_intern
    return union


estate = {
    "RJ": 'Rio de Janeiro',
    "SP": 'São Paulo',
    "MG": 'Minas Gerais',
    "ES": 'Espírito Santo',
    "BA": 'Bahia',
    "MA": 'Maranhão',
    "PB": 'Paraíba'
}


@super_list(*estate.keys())
def zipper(*args: list | tuple):
    return args


my_zip = zipper(*estate.values())
print(*my_zip, sep='\n')
