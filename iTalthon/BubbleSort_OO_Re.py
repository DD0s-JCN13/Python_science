readin = True
raw_data = []
class Bubble_sort(object):
    def __init__(self,list):
        self.list = list
    def sort(self):
        self.
def reader():
    while readin == True:
        getint = input("請輸入要進行分類的數據，或輸入stop結束輸入：")
        if getint == "stop":
            readin = False
        elif format(getint) != "int":
            print("格式錯誤，請重新輸入！")
        else:
            raw_data.append(getint)

