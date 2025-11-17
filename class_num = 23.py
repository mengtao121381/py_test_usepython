"""class_num = 23
avg_salary = 13.22222
message = "当你的职级到%s时，工资可以到%d!"%(class_num, avg_salary)
print(message)"""

# 控制行数
i = 1
while i <= 9:
    # 控制每行的式子数量
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end ='')
        j += 1
    i += 1
    print()