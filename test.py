letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(list(enumerate(letters)))

for i, letter in enumerate(letters):
    stringI = str(i)

    # print(i % 4)

    print(str(i) + " divided by 4 = " + str(i // 4))
    print(str(i) + " divided by 4 = " + str(i / 4))