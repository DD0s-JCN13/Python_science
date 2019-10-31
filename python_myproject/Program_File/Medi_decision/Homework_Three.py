#*-coding:UTF-8
# 類別作業練習 Homework_Three.py (@Tronclass: EX03_hw)
#
# 測試資料 http://140.112.31.82/workpress/?p=216

class student:
    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []
    def add(self, grade):
        self.grades.append(grade)
    def ave(self):
        self.ave = 0
        self.ave = sum(self.grades) / len(self.grades)
        return self.ave
    def fcount(self):
        counter = 0
        for i in self.grades:
            if i < 60:
                counter += 1
        return counter
s1 = student("Tom", "M")
s2 = student("Jane", "F")
s3 = student("John", "M")
s4 = student("Ann", "F")
s5 = student("Peter", "M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

print(s1.ave())
print(s1.fcount())
print(s2.ave())
print(s2.fcount())
print(s3.ave())
print(s3.fcount())
print(s4.ave())
print(s4.fcount())
print(s5.ave())
print(s5.fcount())