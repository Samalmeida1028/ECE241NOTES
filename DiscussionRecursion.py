import random as rand


def recursMultiply(m, n):
    if n > 1:
        return m + recursMultiply(m, n - 1)
    else:
        return m


# need a condition in our recursive function that breaks the loop
# make sure to take care of the var types in our declarations (return same type as inputted)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return alist


def main():
    m = recursMultiply(4, 3)
    print(m)
    n = factorial(5)
    print(n)
    rlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # for i in range(10):
    #   rlist.append(rand.randint(1,1000))

    slist = mergeSort(rlist)
    print(slist)


if __name__ == "__main__":
    main()
