import subprocess
import argparse

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def romanize(input_file, lang, output_file):
    command = f'bin/uroman.pl -l {lang} < {input_file}'
    result = subprocess.check_output([command], shell=True)
    print("Successfully romanized")
    writeFile(output_file, result.decode("utf-8"))
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
    romanize(input_file, L1, output_file)

