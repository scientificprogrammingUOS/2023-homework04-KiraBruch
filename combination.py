import numpy as np 

# implement your function to combine two numpy arrays 

def combine(array1, array2, axis=0):
    # delete the NotImplementedError when you write your function.
    array1 = np.squeeze(array1)
    array2 = np.squeeze(array2)
    try:
        combined = np.concatenate((array1, array2), axis)
        return combined
    except ValueError:
        print("Arrays can not be combined")
    

if __name__ == "__main__":
    # use this for your own testing!

    pass
