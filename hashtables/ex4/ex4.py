def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    i = 0
    step = []
    result = []
    # for i in a:
    #    if i > 0:
    #        if i * -1 in a:
    #            result.append(i)
    a = sorted(a)
    while a[i] < 0 and i < len(a) - 1:
        step.append(a[i])
        i += 1
    for o in step:
        if a.count(o * -1) > 0:
            result.append(o * -1)
        
    return result


if __name__ == "__main__":
    a = [1, 2, 3, -4]

    result = has_negatives(a)
    print(result)
