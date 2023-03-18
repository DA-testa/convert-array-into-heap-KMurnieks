# python3
#Kristaps Mūrnieks 221RDB173
def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        j = i
        # heapifying node i
        while True:
            left = 2 * j + 1
            right = 2 * j + 2
            min_index = j
            if left < n and data[left] < data[min_index]:
                min_index = left
            if right < n and data[right] < data[min_index]:
                min_index = right
            if j != min_index:
                swaps.append((j, min_index))
                data[j], data[min_index] = data[min_index], data[j]
                j = min_index
            else:
                break
    return swaps
            
def main():
    Input = input()
    if "I" in Input:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    if "F" in Input:
        filepath = "tests/" + input();
        with open(filepath, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
            assert len(data) == n
            
            
                    
       # except Exception as ex:
           # print("Error:(", str(ex))
            #return
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    
    # checks if lenght of data is the same as the said lenght
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
