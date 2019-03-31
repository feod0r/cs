# import random
inp = 0
seed = 5

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    # alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "089QRST127UVWXY3456ZABIJCDEFGHKLMNOP"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

def strToInt(num):
    num = str(num)
    buf = 0
    for i in range(0, len(num)):
        buf += abs(ord(num[i])*(seed*i - i))
    return buf

for j in range(1000,1030):
    hash = 0
    inp = j
    inp = convert_base(strToInt(inp),29,13)
    for i in range(0,len(str(inp))):
        # random.seed(i)
        hash = (strToInt(hash << strToInt(convert_base( int(ord(str(inp)[i])**3.5)*i ,31,29)))) + (ord(str(inp)[i])<< (int(ord(str(inp)[i])**0.5)) )
    print(j, inp+convert_base(strToInt(hash),29,13))    # for i in range(0,len(str(inp))):
