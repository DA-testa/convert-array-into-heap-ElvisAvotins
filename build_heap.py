def min_heap(data, k, swaps):
    left = 2 * k + 1
    right = 2 * k + 2

    if left < len(data) and data[left] < data[k]:
        smallest = left
    else:
        smallest = k

    if right < len(data) and data[right] < data[smallest]:
        smallest = right

    if smallest != k:
        data[k], data[smallest] = data[smallest], data[k]
        swaps.append((k, smallest))
        min_heap(data, smallest, swaps)

    return swaps

def build_heap(data):
    n = int((len(data)//2)-1)
    swaps = []

    for k in range(n, -1, -1):
        swaps = min_heap(data,k,swaps)

    return swaps

def main():    
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
