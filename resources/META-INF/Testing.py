print("Hi, Everybody!") # string
print('Good morning')
print("It's a beautiful day in the neighborhood")
print("Today is Saturday and we're doing Python")
print(5)

message = "dogs are dope"
print(message)


num = 1
number = 1

print(num + number)


favNum = 42



message = "my fav num is " + str(favNum)
print(message)


# Conditional execution
doing_python_right_now = True
on_mars_right_now = False
is_raining = False
apples = "delicious"
arr = [1,3,5,2,7]


if doing_python_right_now == True:
    print("Yay Python! Practice makes permanent")
if on_mars_right_now:
    print("How long do you plan to stay on Mars?")
else:
    print("I'm glad we're on Spaceship Earth.")



if is_raining == True:
    print("Bring an umbrella")

if apples == "delicious":
        print ("of course")
else:
        print ("YOU LIE")
print ("ended statement")
print(arr)
arr.sort()
print(arr)
print(sum(arr))
print(len(arr))


def add_one(number):
    result = x+1
    return result
print(add_one(3))


def times_two_plus_three(numberHere):
    return numberHere * 2 + 3
print(times_two_plus_three(10))

def identity(name):
    return name
print(identity("me"))
