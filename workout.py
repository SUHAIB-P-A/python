# reverse integer

num = int(input("enter a number"))
print("orginal num:"+str(num))
rev = 0
while num != 0:
    rem = num % 10
    rev = rev*10+rem
    num //= 10

print("reverse:"+str(rev))


# amstrong or not number

num = int(input("enter a number"))
Armstrong = 0
arm = 0
armlist = []

numstr = str(num)
for i in range(len(numstr)):
    Armstrong = int(numstr[i])**len(numstr)
    print(numstr[i]+"**"+str(len(numstr))+"="+str(Armstrong), end=" ")
    armlist.append(Armstrong)
    arm = arm+Armstrong

print("\n")

for i in range(len(numstr)):
    print(str(armlist[i]), end="")
    if i < len(numstr) - 1:
        print("+", end="")
print("\nresult:"+str(arm))

if (arm == num):
    print("Armstrong")
else:
    print("is not a Armstrong")

# prime or not

num = int(input("enter a number"))
count = 0
for i in range(1, num+1):
    for j in range(1, num+1):
        result = i*j
        # print(result)
        if result == num:
            count += 1
            print(i)
print("count:"+str(count))
if count <= 2:
    print(str(num)+" is a prime number")
else:
    print(str(num)+" is a composite number")
