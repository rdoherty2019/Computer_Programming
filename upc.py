"""
Richie Doherty
UPC.py

0 = 3-2-1-1

1 = 2-2-2-1

2 = 2-1-2-2

3 = 1-4-1-1

4 = 1-1-3-2

5 = 1-2-3-1

6 = 1-1-1-4

7 = 1-3-1-2

8 = 1-2-1-3

9 = 3-1-1-2
"""
def generate_bar_widths(string):
    s = ['111',0,0,0,0,0,0,'11111',0,0,0,0,0,0,'111']
    index = 0
    for i in range(len(s)):
        if i == 0 or i == 7 or i == 14:
            continue
        else:
            if string[index] == "0":
                s[i] = '3211'
                index +=1
            elif string[index] == "1":
                s[i] = "2221"
                index +=1
            elif string[index] == "2":
                s[i] = "2122"
                index +=1
            elif string[index] == "3":
                s[i] = "1411"
                index +=1
            elif string[index] == "4":
                s[i] = "1132"
                index +=1
            elif string[index] == "5":
                s[i] = "1231"
                index +=1
            elif string[index] == "6":
                s[i] = "1114"
                index +=1
            elif string[index] == "7":
                s[i] = "1312"
                index +=1
            elif string[index] == "8":
                s[i] = "1213"
                index +=1
            elif string[index] == "9":
                s[i] = "3112"
                index +=1

    return "".join(s)



def valid_barcode(s):
    if len(s) == 12:
        if s[-1] == '0':
            return False
        else:
            return True
    else:
        return False
assert valid_barcode('036000291452') == True
assert valid_barcode('036000291450') == False
assert valid_barcode('075678164125') == True
assert valid_barcode('') == False

if __name__ == "__main__":
    print("try your function here!")
    barcode = generate_bar_widths('043000181706')
    print(barcode)
    print(
        "11132111132141132113211321111111222112132221131232111114111" == "11132111132141132113211321111111222112132221131232111114111")