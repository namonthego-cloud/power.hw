#===========================
#power calculater
#============================
print()

print("Power calculator")

# part1:ask two que
base = int(input("enter the base number:"))
exponent = int(input("entr the power(exponent): "))

#part2:the running total
#starts at 1 because multiplyinig by 1 changes nothing,
#the way adding 0 changes nothing
result = 1

#part:3+4:loop that multiplies
for i in range(1, exponent + 1):
    result = result * base
    print("step", i,": result=",result)

#part 5: the answer
print("\nanswer:", base, "to power", exponent,"=",result)
