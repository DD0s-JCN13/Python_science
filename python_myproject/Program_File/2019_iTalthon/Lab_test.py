print(3 + 5)

value_1 = 3
value_2 = 5
result_value = value_1 + value_2
print(result_value)

sample = [15, 6, 22, 39, 52, 70]
for x in sample:
    print(x)

print (sample)
list = ["Make", "a", "sample", "here"]
print(list)

#print("Please enter the word you want to print:")
#readin = input()
#print(readin)

fruits = ["香蕉","芭樂","鳳梨","火龍果","蘋果"]
freezed_food = ["冷凍水餃","冰棒","冰淇淋","冷凍三色蔬菜","冷凍湯品"]
meats = ["羊肉","豬肉","牛肉","雞肉","鵝肉"]

def printlist(type): #這就是在Python裡面建立方法的宣告式
    print(type)

printlist(fruits)
printlist(freezed_food)
printlist(meats)

db_float = [4.93, 12.992, 0.97, -2.85337, 3.14159, 21.92]
db_string = ["Showcase", "Police", "thief", "arrest"]
print(db_string)  #先印出原始的陣列排序
db_string.sort()
print(db_string)  #印一個經過基本排序的陣列
db_string.sort(reverse=True) #reverse=True 所以就要把順序顛倒過來
print(db_string)  #這時候印出來的就會是顛倒順序的陣列
def string_len(x):
    return len(x) #在這裡建立一個方法來作為回傳字串的長度
db_string.sort(key=string_len) #套用回傳長度的方法，就會依照字串的長短來排序(預設由小到大)
print(db_string)
db_string.sort(reverse=True, key=string_len) #當然，也可以合併在一起用
print(db_string) #輸出結果就會是以字串長短排序，而且是由大到小來排序

serial_num = ["nac149ac", "nac149xc", "mes177hc", "mes177hxc"]
graphic_card = ["NVMX130", "NVMX150", "NVGTX1070", "NVGTX1080"]
actual_effect = ["NB", "NB", "BES", "AES"]
price = [18900, 21950, 37990, 45900]

def print_compare(sel, graph, actual, cost):
    for comparsion in range(len(sel)):
        print(str(sel[comparsion]), end=' ')
        print(graph[comparsion], end=' ')
        print(actual[comparsion], end=' ')
        print(cost[comparsion])
print_compare(serial_num, graphic_card, actual_effect, price)

pc = {
     "nac149ac": ["NVMX130", "NB", 18900],
     "nac149xc": ["NVMX150", "NB", 21950],
     "mes177hc": ["NVGTX1070", "BES", 37990],
     "mes177hxc":["NVGTX1080", "AES", 45900]
}
def print_sigdata(info):
    for code in range(len(info)):
        print(info[code])
        print(pc[str(info[code])])

print_sigdata(serial_num)

sample_data = [1,29,17,3,22]
def bubble_sort(lst):
    for x in range(0,len(lst)-1):
        booleaner = False
        for y in range(0,len(lst)-1):
            if lst[y] > lst[y+1]:
                tmp = lst[y]
                lst[y] = lst[y+1]
                lst[y+1] = tmp
                booleaner = True
        if booleaner == True:
            print("The " + str(x+1) + " time of exchange: " + str(lst))
        else:
            continue
    print("Final result: " + str(lst))
bubble_sort(sample_data)