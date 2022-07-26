

def generate_dummies(arr):
    zeros_array = []
    # making array of zeros with length n-1
    for i in range(len(arr)-1):
        zeros_array.append(0)

    # making the dictionary
    carClass_dummies = {}

    # making the required dictionary of dummies
    for i in range(len(arr)):
        value = zeros_array.copy()

        if i == 0:
            carClass_dummies[arr[i]] = value

        else:
            value[i-1] = 1
            carClass_dummies[arr[i]] = value

    return carClass_dummies


# Assume that thsi is the array you want to make dummies for
carClass = ["fiat", "hyuandi", "kia", "bmw", "mitsbushi", "honda", "renault"]

print(generate_dummies(carClass))
