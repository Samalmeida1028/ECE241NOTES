def recursMultiply(m, n):
    if (n > 1):
        return m + recursMultiply(m, n - 1)
    else:
        return m

# need a condition in our recursive function that breaks the loop
# make sure to take care of the var types in our declarations (return same type as inputted)

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)




def main():
    m = recursMultiply(4, 3)
    print(m)
    n = factorial(5)
    print(n)


if __name__ == "__main__":
    main()
