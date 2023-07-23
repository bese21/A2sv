def swap_case(s):
    str1=''
    for char in s:
        if char.isupper():
            str1+=char.lower()
        elif char.islower():
            str1+=char.upper()
        else:
            str1+=char
            
    return str1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
