import epitran
import argparse

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def toIPA(input, output, lang):
    contents = readFile(input)
    #print(contents)
    epi = epitran.Epitran(lang)
    result = []
    for line in contents.splitlines():
        parts = line.split("\t")
        parts[0] = epi.transliterate(parts[0])
        parts[1] = epi.transliterate(parts[1])
        result.append('\t'.join(parts))
    result = '\n'.join(result)
    print("Successullty converted to IPA")
    writeFile(output, result)
    print("Completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input file", type=str, required=True)
    parser.add_argument("--output", help="path to output file", type=str, 
    required = True)
    parser.add_argument("--L1", help="input language code", type=str, required=True)
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    L1 = args.L1
    toIPA(input_file, output_file, L1)