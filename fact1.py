def fact(q):
    fun = 1
    while q != 0:
        fun *= q
        q -= 1
    return fun


if __name__ == "__main__":
    print(fact(5))
