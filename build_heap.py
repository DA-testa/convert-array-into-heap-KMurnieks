# python3
#Kristaps Mūrnieks 221RDB173
def heaping(data, i, swaps):
    d = len(data)
    min_index = i
    left = 2*i +1
    if left < d and data[left] < data[min_index]:
        min_index = left
    right = 2*i + 2
    if right < d and data[right] < data[min_index]:
        min_index = right
    
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        heaping(data, min_index, swaps)
    return swaps
        
def build_heap(data):
    x = len(data)
    swaps = []
    for i in range (x // 2-1, -1, -1):
        swaps = swaps + heaping(data, i ,swaps)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)                     
    return swaps
            
            
def main():
    Input = input()
    if "I" in Input:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif "F" in Input:
        filepath = './tests/'
        file = input()
        folder = filepath + file
        try:
            n = int(input())
            data = list(map(int, input().split()))
            assert len(data) == n
                    
        except Exception as ex:
            print("Error:(", str(ex))
            return
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
