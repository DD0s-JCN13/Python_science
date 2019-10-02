print("Testing string")

class BubbleSort(object):
    read_in = True
    after_sort = []
    def __init__(self, list):
        self.list = list
    def sort(self):
        self.after_sort = self.list
        for x in range(0, len(self.after_sort) - 1):
            booleaner = False
            for y in range(0, len(self.after_sort) - 1):
                if self.after_sort[y] > self.after_sort[y + 1]:
                    tmp = self.after_sort[y]
                    self.after_sort[y] = self.after_sort[y + 1]
                    self.after_sort[y + 1] = tmp
                    booleaner = True
            if booleaner == True:
                print("After " + str(x + 1) + " time(s) of exchange: " + str(self.after_sort))
            else:
                continue
    def print_origin(self):
        print("The original list: " + str(self.list))
    def printer(self):
        print("The result afte Bubble Sort is: " + str(self.after_sort))

test1 = BubbleSort([12,8,27,5,13,6,21])
test1.print_origin()
test1.sort()
test1.printer()