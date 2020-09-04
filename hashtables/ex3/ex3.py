def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    obj = {}

    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            if arrays[i][j] in obj:
                obj[arrays[i][j]].append(i)
            else:
                obj[arrays[i][j]] = [i]
    return obj



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

print(intersection(arrays))