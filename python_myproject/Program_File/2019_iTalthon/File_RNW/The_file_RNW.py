file_tester = open("Testing_text.txt", "w")
"""上面這行程式碼其實是用來指定要進行讀寫的檔案"""
file_tester.write("Say hello to python_myproject competitors!")
file_tester.close()
file_reader = open("Testing_text.txt", "r")
print(file_reader.readline())
file_reader.close()
