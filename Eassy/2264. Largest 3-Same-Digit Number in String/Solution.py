def largestGoodInteger(num: str) -> str:
    max_good = ""
    for i in range(len(num) - 2):
        substring = num[i:i+3]
        if substring[0] == substring[1] == substring[2]:  # all digits same
            if substring > max_good:  # lexicographic works for digits
                max_good = substring
    return max_good
