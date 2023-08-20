income = int(input("請輸入今年收入淨額: "))
if income >= 300_000:
    if income >=2_000_000:
        incometax = income *0.3
    elif income >= 1_000_000:
        incometax = income * 0.21
    elif income >= 600_000:
        incometax = income * 0.13
    else:
        incometax = income * 0.06
        
else:
    incometax = 0

print("應付稅額:"+ str(incometax))