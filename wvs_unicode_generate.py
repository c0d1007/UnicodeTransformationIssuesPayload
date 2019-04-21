def unicode_encode(s):
    result = ''
    for c in s:
        '''
        print(urllib.quote(c))
        print(hex(ord(c)))
        print(hex(ord(c) + 0x80))
        '''
        if 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            result += c
        else:
            result += '%C0%' + str(hex(ord(c) + 0x80)).split('x')[1].upper()

    print(result)

if __name__ == '__main__':
    s = input('please input change string:\n')
    unicode_encode(s)
