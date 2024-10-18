def finding_highest(var1, var2, var3, var4, var5):
    if var1 >= var2 or var2 >= var3 or var3 >= var4 or var4 >= var5:
        if var1 >= var2 and var1 >= var3 and var1 >= var4 and var1 >= var5:
            return var1
        elif var2 >= var1 and var2 >= var3 and var2 >= var4 and var2 >= var5:
            return var2
        elif var3 >= var1 and var3 >= var2 and var3 >= var4 and var3 >= var5:
            return var3
        elif var4 >= var1 and var4 >= var2 and var4 >= var3 and var4 >= var5:
            return var4
        elif var5 >= var1 and var5 >= var2 and var5 >= var3 and var5 >= var4:
            return var5
        else:
            if var1 <= var2 or var2 <= var3 or var3 <= var4 or var4 <= var5:
                if var1 >= var2 and var1 >= var3 and var1 >= var4 and var1 >= var5:
                    return var1
                elif var2 >= var1 and var2 >= var3 and var2 >= var4 and var2 >= var5:
                    return var2
                elif var3 >= var1 and var3 >= var2 and var3 >= var4 and var3 >= var5:
                    return var3
                elif var4 >= var1 and var4 >= var2 and var4 >= var3 and var4 >= var5:
                    return var4
                else:
                    return var5
var1 = (int(input("Please enter num1: ")))
var2 = (int(input("Please enter num2: ")))
var3 = (int(input("Please enter num3: ")))
var4 = (int(input("Please enter num4: ")))
var5 = (int(input("Please enter num5: ")))
num = finding_highest(var1, var2, var3, var4, var5)
print(f"The highest number is {num}")