"""python program to find number of letters that would be used to write """
words_dict = {
    100000000: "billion",
    1000000: "million",
    1000: "thousand",
    100: "hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "forty",
    30: "trirty",
    20: "twenty",
    19: "ninteen",
    18: "eighteen",
    17: "seventeen",
    16: "sixteen",
    15: "fifteen",
    14: "fourteen",
    13: "thirteen",
    12: "twelve",
    11: "eleven",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
}


def find_length(num):
    """function to find lenght of each number in words"""
    if num == 0:
        return 0
    if num in words_dict:
        return len(words_dict[num])
    ans = 0
    if len(str(num)) == 3 and num % 100 != 0:
        ans += 3
    for obj in words_dict.items():
        if num >= obj[0]:
            if num >= 100:
                ans += find_length(num // obj[0])
            ans += len(obj[1]) + find_length(num % obj[0])
            return ans
    return 0


def solver(n: int = 1, m: int = 1000):
    """function to find length of all number in words"""
    ans = 0
    for i in range(n, m + 1):
        ans += find_length(i)
    return ans


if __name__ == "__main__":
    print(solver(1, 1000))
