print(int(0b0))
print(bin(26))

origin = 0b101 #也就是5
set_left = origin << 2 #透過將origin向左平移兩位來使其值變大
set_right = origin >> 1 #相對的，透過將origin向右平移兩位來使其值變小
print(bin(origin))
print(bin(set_left))
print(bin(set_right))
print(int(origin))
print(int(set_left))
print(int(set_right))

setter = 0b110010 #32+16+2=50
testing = 0b101010 #32+8+2=42

and_test = setter & testing #使用and運算元
or_test = setter | testing #使用or運算元
nor_test = setter ^ testing #使用nor運算元
print(bin(and_test))
print(bin(or_test))
print(bin(nor_test))

