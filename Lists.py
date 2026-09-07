# CODING 1 - CREATING A LIST

numbers = [2, 4, 6, 8, 10]
colors = ["Red", "blue", "pink", "yellow", "black"]
combined_list = [109, 80.9, "Sowmya", True]
empty_list = []

print(numbers, colors, combined_list, empty_list)


# CODING 2 - ACCESSING LIST ELEMENTS

colors = ["Red", "blue", "pink", "yellow", "black"]

print(colors[0])
print(colors[-5])
print(colors[4])
print(colors[-1])


# CODING 3 - MODIFY A LIST

colors = ["Red", "blue", "pink", "yellow", "black"]

colors[1] = "Lavender"
colors[2] = "Green"

print(colors)


# CODING 4 - COMMON LIST OPERATIONS

colors = ["Red", "blue", "pink", "yellow", "black"]

colors.append("White")
colors.insert(1, "Orange")

print(colors)


# CODING 5 - COMMON LIST OPERATION

colors = ["Red", "blue", "pink", "yellow", "black"]

colors.pop()

print(colors)


# CODING 6 - COMMON LIST OPERATION

colors = ["Red", "blue", "pink", "yellow", "black"]

colors.remove("Red")

print(colors)


# CODING 7 - LENGTH OF LIST

colors = ["Red", "blue", "pink", "yellow", "black"]
combined_list = [109, 80.9, "Sowmya", True]

print(len(colors))
print(len(combined_list))


# CODING 8 - BUILT-IN FUNCTIONS IN LIST

a = [5, 34, 98, 20, 25]

print(min(a))
print(max(a))

a.sort()
print(a)

a.reverse()
print(a)


# CODING 9 - LOOPING IN LIST

colors = ["Red", "blue", "pink", "yellow", "black"]

for i in colors:
    print(i)


# CODING 10 - LIST SLICING

a = [5, 34, 98, 20, 25]

print(a[0:2])
print(a[::-1])


# CODING 11 - SQUARE OF NUMBERS FROM RANGE 1 TO 5

s = [n ** 2 for n in range(1, 6)]

print(s)


# CODING 12 - SQUARE OF NUMBERS

l1 = [5, 2, 4, 7, 8]

s = [n ** 2 for n in l1]

print(s)


# CODING 13 - COUNT EVEN NUMBERS

z = [3, 8, 9, 10, 45, 22]
w = 0

for n in z:
    if n % 2 == 0:
        w += 1

print(w)


# CODING 14 - LIST OPERATIONS

student = []

student.append("Sowmya")
student.append("Maggi")
student.append("Damen")
student.append("Nanthini")

for i in student:
    print(i)

student.insert(1, "Kiranya")
print(student)

student.remove("Sowmya")
print(student)

student.sort()
print(student)

for i in student:
    print(i)

a = input("Enter the name: ")

for i in student:
    if i == a:
        print("The name is present in the list")
        break
else:
    print("The name is not present in the list")


# CODING 15 - REMOVING DUPLICATES

x = [2, 5, 6, 9, 5, 2, 10]
y = ["Damen", "Sowmya", "Maggi", "Nanthini"]

print(set(x))
print(set(y))
