# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    for i in files:
        for o in queries:
            if i.rsplit('/',1)[1] == o:
                result.append(i)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
