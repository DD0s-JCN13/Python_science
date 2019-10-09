#程式目標：設計一個百貨公司在周年慶時，用來辨識會員資料的功能
#其中，會員身分有分級，在進行購物時會因為自己的會員等級而享有不同的折扣
class Sogo(object):
    #預先設定基本值：一般會員，享有9折優惠，會存取會員的名字
    def __init__(self, total_cost, customer_name):
        self.discount = 0.9
        self.total_cost = total_cost
        self.customer_name = customer_name
    def printer(self):
        print("Hello, " + str(self.customer_name) + ", what do you want to buy today?")
    def check_out(self):
        return "The total is " + str(self.total_cost * self.discount)
    def print_check_out(self):
        print(Sogo.check_out(self))

class sliver_member(Sogo):
    #隨著會員等級的不同，系統也會有不一樣的問候語，這個設定是銀級會員的
    def __init__(self, total_cost, customer_name):
        self.discount = 0.85
        self.total_cost = total_cost
        self.customer_name = customer_name
    def printer(self):
        print("Welcome back, " + str(self.customer_name) + ", we have some discount for you today.")
    def check_out(self):
        #設定每個會員等級的結帳後問候語不同，在這裡就先引用一般會員的結帳問候語，然後再做改變
        return Sogo.check_out(self) + ", see you next time."
    def print_check_out(self):
        print(sliver_member.check_out(self))

class gold_member(sliver_member):
    #這個則是設定金級會員的
    def __init__(self, total_cost, customer_name):
        self.discount = 0.75
        self.total_cost = total_cost
        self.customer_name = customer_name
    def printer(self):
        print("Welcome back, " + str(self.customer_name) + ", how can we help you today?")
    def check_out(self):
        #同理，這裡也一樣做點變化
        return Sogo.check_out(self) + ", please come to VIP room to have some gifts."
    def print_check_out(self):
        print(gold_member.check_out(self))

CM1 = Sogo(28000, "Nick")
CM1.printer()
CM1.print_check_out()
print("")
SM1 = sliver_member(29000, "Linda")
SM1.printer()
SM1.print_check_out()
print("")
GM1 = gold_member(49000, "Wendy")
GM1.printer()
GM1.print_check_out()


