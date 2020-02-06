from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
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

transliterate_text("2019-master/task1/sanskrit--bengali/sanskrit-train", "sanskrit-to-Bengali&Bengali/sanskrit-bengali", "sa", "bn")
