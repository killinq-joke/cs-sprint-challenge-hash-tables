from hashtable import HashTable

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    obj = {}
    for i in range(length):
        obj[weights[i]] = i
    for i in range(length):
        if (limit - weights[i]) in obj:
            if limit == weights[i] * 2:
                arr = []
                for o in range(length):
                    if weights[o] == weights[i]:
                        arr.append(length - o - 1)
                return arr
            return [obj[limit - weights[i]], obj[weights[i]]]
    return None

print(get_indices_of_item_weights([ 4, 4 ], length = 2, limit = 8))