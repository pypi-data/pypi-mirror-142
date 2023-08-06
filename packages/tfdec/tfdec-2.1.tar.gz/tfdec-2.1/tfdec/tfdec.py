def baseToBase(number: str, baseFrom=10, baseTo=10) -> str:
    '''
    basetoBase(number, baseFrom=10, baseTo=10)

    Convert number from one radix to second radix. Optional keyword arguments:
    baseFrom: the radix from which you want to convert the number; default is 10.
    baseTo: the radix to which you want to convert the number; default is 10.
    '''
    abc, s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', ''
    try: number = int(number, baseFrom)
    except: return -1
    if any(str(number)) > baseTo: return -1
    while number > 0: s = abc[number%baseTo] + s; number //= baseTo
    return s