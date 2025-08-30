# print(str("5") + str("6"))

# x = 30
# y = 40
# z = 21  
# print(str(z) + str(x+y))

# x = [1, 2, 3]
# y = x[1] * 5
# print(x[0] + y - x[2])

# name = "john"
# x = name[0] + name[3]
# y = x + name[1]
# print(y + name[2])

# x = [1,2,3]
# y = len(x) * 5
# z = y * 2
# print(z)

# x = "7&11"
# y = int(x[0])
# z = x[0] + x[2]
# print(y + int(z))

# x = [16,7,8]
# x.append(13)
# x.remove(16)
# z = 16 + x[2]
# print(z)

# x = 3 + 8 * 8
# y = x + 7 +8
# print(x)

# def sum(x ,y):
#     return x + y
# print(sum(8,3) + 18)

# def doubleSum(x, y):
#     return 2 * (x + y)

# def sum(x, y):
#     return x + y
# print(doubleSum(2,10) + sum(10, 10))

# def doublesum(x,y):
#     return 2 * (x+y)
# def sum(x,y):
#     return doublesum(x,y) + x

# print(sum(12,10))
# print(1 + 1)

my_age = 25
def checkage(age):
    if age > 17:
        return "qualified"
    else:
        return  "not qualified"
    
print(checkage(my_age)[2])

passWord = "Hello123"
def x(a,b, passWord):
    haha = passWord[a] + passWord[b]
    return haha
print(x(4,6, passWord))
