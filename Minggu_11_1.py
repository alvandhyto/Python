def bar(SIZE):
    print("#" + 4 * SIZE * "=" + "#")


def mirror(SIZE):
    list_a = list(range(1, SIZE + 1))
    list_b = list(range(SIZE, 0, -1))
    list_ab = list_a + list_b

    for line in list_ab:
        print("|" + (-2 * line + 2 * SIZE) * " " + "<>" + (4 * line - 4) * "." + "<>" + (
                -2 * line + 2 * SIZE) * " " + "|")


SIZE = int(input("Masukkan Size: "))

for i in range(SIZE + 1):
    print("Size " + str(i))
    bar(i)
    mirror(i)
    bar(i)
    print()
