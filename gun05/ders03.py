def birinci():
    print("birinci çalıştı")
    return ikinci()
def ikinci():
    print("ikinci çalıştı")
    return ucuncu()

def ucuncu():
    print("üçüncü çalıştı")

if __name__ == '__main__':
    print("hello world")
    a = birinci()
    print(a)
