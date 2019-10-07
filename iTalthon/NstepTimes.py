def NstepMode(read_in):
    if type(read_in) is not int:
        print("格式錯誤，請重新執行程式！")
    if read_in < 0:
        print("N階乘最小值為 0! = 1，小於0之階乘不存在")
    elif read_in == 0:
        return 1
    else:
        return read_in * NstepMode(read_in-1)

print(NstepMode(5))