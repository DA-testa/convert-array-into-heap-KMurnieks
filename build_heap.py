# python3


def build_heap(data):
    d = len(data)
    swaps = []
    for i in range (d/2-1, -1, -1):
        swaps = swaps + heaping(data, i ,d)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps
    
    def heaping(data, i):
        swaps = []
        left = 2*i+1
        right = 2 * i +2
        smallest = i
        if left < d and data[left] < data[smallest]:
            smallest = left
        if right < d and data[right] < data[smalleest]:
            smallest = right
        
        if smallest != i:
            swaps.append((i, smallest))
            data[i], data[smallest] = data[smallest], data[i]
            swamps = swaps heaping(data, smallest)
            
        return swaps
            
            
def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
