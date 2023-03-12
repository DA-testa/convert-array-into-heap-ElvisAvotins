def min_heap(A, k, swaps):
    left = 2 * k + 1
    right = 2 * k + 2
    if left < len(A) and A[left] < A[k]:
        smallest = left
    else:
        smallest = k
    if right < len(A) and A[right] < A[smallest]:
        smallest = right
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        swaps.append((k, smallest))
        min_heap(A, smallest, swaps)
    return swaps

def build_heap(data):
    n = int((len(data)//2)-1)
    swaps = []
    for k in range(n, -1, -1):
        swaps = min_heap(data,k,swaps)
    return swaps

def main():    
    size = 0
    arr = []
    file_or_input = input().strip().lower()
    
    if file_or_input == "i":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i in swaps:
            print(i[0], i[1])

    elif file_or_input == "f":
        file_name = input().strip()

        if 'a' in file_name:
            return
        file_path = ("tests/" + file_name)

        with open(file_path, encoding="utf8") as f:
            n = int(f.readline())
            line = f.readline().strip()
            data = [int(x) for x in line.split()]
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i in swaps:
            print(i[0], i[1])

    else:
        quit()

if __name__ == "__main__":
   main()
