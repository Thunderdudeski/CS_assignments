import numpy as np

def main():
    array = np.random.randint(0,100,(5,5))
    print(f"The full array is: \n{array}")
    print(f"The 2nd row 3rd column item is: {array[1][2]}")
    print(f"Total sum of all numbers in array is: {np.sum(array)}")
    print(f"The mean of each row is: {np.mean(array, axis=1)}")
    print(f"The max of each column is: {np.max(array, axis=0)}")



if __name__ == '__main__':
    main()