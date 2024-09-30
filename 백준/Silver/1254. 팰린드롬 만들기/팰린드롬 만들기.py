def solutions():
    a = input()
    al = len(a)  # O(1)
    # O(N^2)
    for i in range(len(a)):  # O(N)
        b = a[i::]  # O(N)
        c = b[::-1]  # O(N)
        if b == c:
            print(al+i)
            break
    

if __name__ == '__main__':
    solutions()
