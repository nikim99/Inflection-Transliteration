import argparse


def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def compare(test, gold, baseline, output):
    testContents = readFile(test)
    goldContents = readFile(gold)
    baseContents = readFile(baseline)
    result = []
    testLines = testContents.splitlines()
    goldLines = goldContents.splitlines()
    baseLines = baseContents.splitlines()
    totalCounts = {}
    wrongCounts_test = {}
    wrongCounts_base = {}
    numWrong_test = 0
    numWrong_base = 0
    for i in range(len(testLines)):
        testParts = testLines[i].split("\t")
        goldParts = goldLines[i].split("\t")
        baseParts = baseLines[i].split("\t")
        if testParts[1] != goldParts[1]:
            numWrong_test += 1
            #result.append(testParts[0] + "\t" + testParts[2])
            tags = goldParts[2].split(";")
            for tag in tags:
                wrongCounts_test[tag] = wrongCounts_test.get(tag, 0) + 1
                totalCounts[tag] = totalCounts.get(tag, 0) + 1
        else:
            tags = goldParts[2].split(";")
            for tag in tags:
                totalCounts[tag] = totalCounts.get(tag, 0) + 1
        if baseParts[1] != goldParts[1]:
            numWrong_base += 1
            tags = goldParts[2].split(";")
            for tag in tags:
                wrongCounts_base[tag] = wrongCounts_base.get(tag, 0) + 1
    summary = []
    for tag in wrongCounts_test:
        tagInfo = f'{tag}: {abs((wrongCounts_test[tag]/totalCounts[tag]) - (wrongCounts_base[tag]/totalCounts[tag]))}'
        summary.append(tagInfo)
    output_contents = f'Accuracy test: {1 - numWrong_test/len(goldLines)}\n' + \
        f'Accuracy baseline: {1 - numWrong_base/len(goldLines)}\n\n' + \
        'Ratio of tags of incorrectly generated inflections minus baseline ratio: \n' + \
         "\n".join(summary) + "\n\n" #+ "Incorrect words: \n" + "\n".join(result)
        
    writeFile(output, output_contents)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", help="path to ftest file", type=str, required=True)
    parser.add_argument("--gold", help="path to gold file", type=str, 
    required = True)
    parser.add_argument("--baseline", help="path to baseline file", type=str, 
    required = True)
    parser.add_argument("--output", help="path to output file", type=str, required=True)
    args = parser.parse_args()
    test = args.test
    gold = args.gold
    output = args.output
    baseline = args.baseline 
    compare(test, gold, baseline, output)