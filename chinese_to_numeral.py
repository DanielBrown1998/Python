def to_chinese_numeral(n):
    numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }

    if n < 0:
        num_int = int(-1*n)
        num_frac = str(round(-1*n - num_int, 3))
    else:
        num_int = int(n)
        num_frac = str(round(n - num_int, 3))
    num_int = str(num_int)

    num_int_chinese = ""
    num_frac_chinese = ""
    if n >= 1:
        for i in range(len(num_int)):
            if num_int[i] == "0" and num_int_chinese[-1] == numerals[0]:
                continue
            num_int_chinese += numerals[int(num_int[i])]
            if i < len(num_int) - 1 and num_int[i] != '0':
                num_int_chinese += numerals[10**(len(num_int) - i - 1)]
    for i in range(2, len(num_frac)):
        num_frac_chinese += numerals[int(num_frac[i])]
    
    if n < 0:
        num_int_chinese = numerals["-"] + num_int_chinese

    if num_int_chinese:
        if num_int_chinese[-1] == numerals[0]:
            num_int_chinese = num_int_chinese[:-1]

    if isinstance(n, float):
        if not num_int_chinese:
            num_int_chinese = numerals[0]            
        return num_int_chinese + numerals["."] + num_frac_chinese
    else:
        return num_int_chinese


num = 102.32
num = to_chinese_numeral(num)
print(num) # 一百零二点三二
num = 9
num = to_chinese_numeral(num)
print(num) # 九
num = -5
num = to_chinese_numeral(num)
print(num) # 负五