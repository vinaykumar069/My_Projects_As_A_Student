import random
print("--------You only have 3 chances after losing first attempt--------")
r = random.randint(1,100)
x=int(input("\nGuess the Number b/w 1-100\n"))
while x>100 or x<1:
    print("ValueError")
    x=int(input("guess again : "))
def xcheck(x):
    if x==r:
        return 1
def xcompare(x):
    if x<r:
        return "Too Low"
    else:
        return "Too High"
for i in range(3):
    if xcheck(x):
        print("You Win!")
    else:
        print(xcompare(x))
        j=0
        print("Do you want to try again?(yes/no)")
        option = input().lower()
        if option=="yes":
             j=1
        else:
            j=0
        if j==1:
         x=int(input("Enter again"))
        if xcheck(x):
             print("You Win!")
        else:
            print("You lost!")