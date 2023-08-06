def baseToBase(num: str, baseFrom=10, baseTo=10) -> str:
    abc, s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', ''
    try: num = int(num, baseFrom)
    except: return -1
    if any(str(num)) > baseTo: return -1
    while num > 0: s = abc[num%baseTo] + s; num //= baseTo
    return s