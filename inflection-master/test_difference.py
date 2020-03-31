
'''
Determines the difference in characters between two files.
'''


# From https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()


def test_difference(path1, path2):
    file1 = readFile(path1)
    file2 = readFile(path2)
    file1Seen = set()
    file2Seen = set()
    for c in file1:
        file1Seen.add(c)
    for c in file2:
        file2Seen.add(c)
    print("In Original Test but not Uncovered Normalized: ", file1Seen.difference(file2Seen))
    print("In Uncovered Normalized but not Original Test: ", file2Seen.difference(file1Seen))
    print(file1 == file2)

test_difference("outputs/hindi-bengali-bengali/orig.test.output", "outputs/hindi-bengali-bengali/bengali-test-norm")
