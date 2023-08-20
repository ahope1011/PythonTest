month = int(input("請輸入月份:"))
if (1 <= month <= 3):
    print(str(month)+ "月是春天")
elif (4 <= month <= 6):
    print(str(month)+ "月是夏天")
elif (7 <= month <= 9):
    print(str(month)+ "月是秋天")
elif (10 <= month <= 12):
    print(str(month)+ "月是冬天")
else:
    print("這個不在範圍內")