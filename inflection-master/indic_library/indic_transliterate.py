from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
import argparse


# From https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def transliterate_text(input_file, output_file, input_lang, output_lang):
    input_text = readFile(input_file)

    #Normalize
    remove_nuktas = False
    factory=IndicNormalizerFactory()
    normalizer=factory.get_normalizer(input_lang,remove_nuktas)
    normalized = normalizer.normalize(input_text)
    print("Text Normalized")
    #Transliterate
    transliterated = UnicodeIndicTransliterator.transliterate(normalized,
                     input_lang,output_lang)
    print("Text Transliterated")
    writeFile(output_file, transliterated)
    print("Completed")

def normalizer_text(input_file, output_file, input_lang):
    input_text = readFile(input_file)

    #Normalize
    remove_nuktas = False
    factory=IndicNormalizerFactory()
    normalizer=factory.get_normalizer(input_lang,remove_nuktas)
    normalized = normalizer.normalize(input_text)
    print("Text Normalized")
    writeFile(output_file, normalized)
    print("Completed")
    
#normalizer_text("bengali-test", "bengali-test-norm", "bn")
#transliterate_text("2019-master/task1/hindi--bengali/hindi-train", "sanskrit-to-Bengali&Bengali/sanskrit-bengali", "hi", "bn")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input file", type=str, required=True)
    parser.add_argument("--output", help="path to output file", type=str, 
    required = True)
    parser.add_argument("--L1", help="input language code", type=str, required=True)
    parser.add_argument("--L2", help="output language code", type=str, required=True)
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    L1 = args.L1
    L2 = args.L2
    transliterate_text(input_file, output_file, L1, L2)
