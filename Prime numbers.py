# I) CHECK WHETHER A GIVEN NUMBER IS PRIME OR NON-PRIME

n = int(input("Enter a Number: "))
c = 0

for i in range(1, n + 1):
    if n % i == 0:
        c += 1

if c == 2:
    print(n, "It is a Prime Number")
else:
    print(n, "It is not a Prime Number")


# II) PRIME NUMBERS WITHIN AN INTERVAL USING FOR LOOP

for i in range(1, 101):
    c = 0

    for j in range(1, i + 1):
        if i % j == 0:
            c += 1

    if c == 2:
        print(i)


# III) PRIME NUMBERS WITHIN AN INTERVAL USING WHILE LOOP

i = 1

while i < 100:
    i += 1
    c = 0

    for j in range(1, i + 1):
        if i % j == 0:
            c += 1

    if c == 2:
        print(i)
