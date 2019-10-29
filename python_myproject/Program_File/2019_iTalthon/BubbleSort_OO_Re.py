class Bubble_sort(object):
    def __init__(self,lister):
    #建構基礎物件的形式
        self.lister = lister
    def sort(self):
    #核心部分之一：Bubble Sort方法
        self.sorter = self.lister
        for x in range(0, len(self.sorter) - 1):
            booleaner = False
            #這個booleaner參數，其實是為了要把「有進行」交換的狀態進行輸出而設定的
            for y in range(0, len(self.sorter) - 1):
                if self.sorter[y] > self.sorter[y + 1]:
                    tmp = self.sorter[y]
                    self.sorter[y] = self.sorter[y + 1]
                    self.sorter[y + 1] = tmp
                    booleaner = True
            if booleaner == True:
                print("After " + str(x + 1) + " time(s) of exchange: " + str(self.sorter))
            else:
                continue
        return self.sorter
        #在最後將「已完成排序」的List進行回傳
    def print_origin(self):
        print("Your input is: " + str(self.lister))
        #印出由使用者輸入的資料原始狀態
    def print_after(self):
        print("The result after Bubble Sort is: " + str(Bubble_sort.sort(self)))
        #印出已完成排序的資料
        #後面那串str(Bubble_sort.sort(self))之所以會是這樣
        #是因為前面有輸出其他字串，所以要轉成str屬性，然後透過物件導向的方法得到資料

raw_data = []
readin = True
#驅使下方的reader方法運作的布林值
def reader(readin):
    while readin == True:
    #使用while迴圈，確保使用者不會在尚未輸入完資料的時候就停止
        getint = input("請輸入要進行分類的數據，或輸入stop結束輸入：")
        if getint == "stop":
            readin = False
        else:
            x = getint.format(int)
            #先做第一步的格式轉換，但其實透過下方的isdigit()就可以辨識了
            if x.isdigit() is False:
                print("格式錯誤，請重新輸入！")
            else:
                raw_data.append(x)
    else:
    #這裡就是當while迴圈結束之後要進行的其他步驟
        runner = Bubble_sort(raw_data)
        runner.print_origin()
        runner.sort()
        runner.print_after()
reader(readin)
#整個程式驅動的起點