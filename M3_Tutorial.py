'''Alexander Schalk
SDEV 220 - Evan Mitchell
M3 Programming Assignment
04/08/2024
'''

#Binary Sort

def sort012(arr, N):
    '''Sorts an array of 0s, 1s, and 2s. N Is length of array'''
    i = 0
    for x in arr: #Jump to first non zero
        if x == 0: i += 1
        else: break

    while i < N:
        print(i, arr)
        if arr[i] == 0:  #Move the 0 to beginning of the list
            arr.insert(0, arr.pop(i))
        elif arr[i] == 2: #Move the 2 to the end of the list
            arr.insert(N, arr.pop(i))
            N -= 1 #Unnecesary to search the 2s multiple times
        else:
            i += 1 #Element is a 1, check next element
    return(arr)

def binary_sort(itera, target): 
    '''Binary Sort function. It should receive an iterable and a value that is within that iterable.'''
    index = len(itera)//2 #Creating an "I" for the while loop 
    top = len(itera) #Highest found elements index
    bottom = 0 #Lowest found elements index
    while True:
        if itera[index] ==  target: return(index) #We found it
        elif itera[index] > target: #Our guess was too big, search top half
            bottom = target
            index = (index + top)//2
        else: #Our guess was too small
            top = target
            index = (index + bottom)// 2












