class RomanNumerals:

    @staticmethod
    def to_roman(num: int) -> str:
        nums_roman = ['nan', 'M', "CM", 'D', 'DC', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [0, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_num = ''
        for pos, number in enumerate(nums[1:]):
            pos += 1
            if number > num:
                continue
            if num//number not in list(range(10)):
                roman_num += num//number * nums_roman[nums.index(num - (num % number))]
            else:
                roman_num += num//number * nums_roman[pos]
            num = num % number

        return roman_num

    @staticmethod
    def from_roman(roman_num: str) -> int:
        num = 0
        nums_roman = ['nan', 'M', "CM", 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [0, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for items in ['CM', 'DC', 'XC', 'XL', 'IX', 'IV']:
            if items in roman_num:
                num += nums[nums_roman.index(items)]
                pos = roman_num.find(items)
                caracteres = list(c for c in roman_num)
                caracteres.pop(pos)
                caracteres.pop(pos)
                roman_num = ''.join(caracteres)
        for item in roman_num:
            num += nums[nums_roman.index(item)]

        return num


if __name__ == '__main__':
    numbers = RomanNumerals()
    print(numbers.to_roman(2131))
    print(numbers.from_roman('MMCXXXI'))
    print(numbers.from_roman('IV'))
    print(numbers.from_roman('XIX'))
