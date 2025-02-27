print("------------Calculator-------------")
print("Enter your statement ")
statement = input("(*_*)\n")

def addition(temp):
    l=len(temp)
    result = 0
    for i in range(0,l):
        result = float(result) + float(temp[i])
    return result
def subtraction(temp):
    l=len(temp)
    result = int(temp[0])
    for i in range(0,l-1):
        result = float(result) - float(temp[i+1])
    return result
def multliplication(temp):
    l=len(temp)
    result = 1
    for i in range(0,l):
        result = float(result) * float(temp[i])
    return result
def division(temp):
    l=len(temp)
    result = float(temp[0])
    for i in range(0,l-1):
        result = float(result)/float(temp[i+1])
    return result
    

if("+" in statement):
    values = statement.split("+")
    result = addition(values)
    print("Result=",result)
elif("-" in statement):
    values = statement.split("-")
    result = subtraction(values)
    print("Result=",result)
elif("*" in statement):
    values = statement.split("*")
    result = multliplication(values)
    print("Result=",result)
else:
    values = statement.split("/")
    result = division(values)
    print("Result=",result)
    