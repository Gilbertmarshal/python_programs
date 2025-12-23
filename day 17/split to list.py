if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))


reversed_arr = arr[::-1]

print(*reversed_arr)
