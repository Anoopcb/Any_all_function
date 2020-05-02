##Any(), All() function

number1 = [2, 4, 6, 8, 10]
number2 = [1, 3, 5, 7, 9]

even1 = []

for i in number1:
    even1.append(i%2==0)
print(even1)

print(all([True, True, True, True, True]))

print(all([i%2!=0 for i in number2]))

print(all([i%2==0 for i in number2]))## all will give you true if all value are true in the lise

## or false if any false is there



###Any function

## any fuction will give true if there is any ture in the list

def my_sum(*args):

    total = 0

    for i in args:

        total +=i
    return  total

print(my_sum(1, 2, 3, 5, 4, 6))


def my_sum(*args):
    if all([(type(arg) == int or type(arg)==float) for arg in args]):
        total = 0

        for i in args:
            total += i
        return total
    else:
        return "worng input"


print(my_sum(1, 2, 3, 5, 4, 6, "Anoop", ["Pi", 2.25]))

