import pandas as pd
import numpy as np
Student = ["王曉明", "李小美", "陳小華", "蔣小偉"]
#new_Student = ["Linda", "Jacky", "Wade", "Mandy"]
Attendance = [48, 75, 70, 50]
Quiz = [68, 52, 60, 43]
Final_exam = [56, 40, 39, 26]
Average = np.array(Attendance) * 0.25 + np.array(Quiz) * 0.3 + np.array(Final_exam) * 0.4
Changed = Average ** 0.5 * 9.52

Math_score = {"Students": Student,
              "Attendance": Attendance,
              "Quizzes": Quiz,
              "Final_exam": Final_exam,
              "Average": Average,
              "Changed_score": Changed}
"""new_Math_score = {"Students": new_Student,
                  "Attendance": Attendance,
                  "Quizzes": Quiz,
                  "Final_exam": Final_exam,
                  "Average": Average,
                  "Changed_score": Changed}"""
print(pd.DataFrame(Math_score))
#print(pd.DataFrame(new_Math_score))

write_in = open("Score_save.txt", "w")
write_in.write(str(pd.DataFrame(Math_score)))
write_in.close()

reader = open("Score_save.txt", "r")
print(reader.read())
reader.close()

