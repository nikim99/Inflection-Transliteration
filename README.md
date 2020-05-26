# Inflection-Transliteration
This is the code accompanying our paper "Transliteration for Cross-Lingual Morphological Inflection" (link to come).

## Requirements
Requires the following libraries:
- ["Indic NLP Library"](https://github.com/anoopkunchukuttan/indic_nlp_library)
- ["Epitran"](https://github.com/dmort27/epitran)
- ["URoman"](https://github.com/isi-nlp/uroman)
- ["antonisa/inflection"](https://github.com/antonisa/inflection)

## Inflection
To run the inflection model of antonisa/inflection, follow the path: inflection_master/inflection.py
To run the file, follow the instructions their page, using the default settings.
Options:
-For --mode, use either train or test depending on whether you are training the model or testing it
-For --L1, keep a comma seperated list of the transfer language in the ISO 639-2 language code forms.
-For --L2, use the ISO 639-2 language code form of the test language
-For --use_hall, only include this tag if you want to include hallucinated data
-For the --predict_lang, --use_att_reg, and --use_tag_reg, these are optional tags you can include to see if any improve performace. For details on what these tags do, redirect to inflection page. In our experiments we found, that the --use_att_reg and --use_tag_reg work best for when transliteration into the test script as a pre-processing step. For using romanization or IPA transcription, using none of these additional tags seemed to work best. 

## Indic Transliteration
To get to the Indic Transliteration file follow the path: inflection_master/indic_library/indic_transliterate.py
To run the file, run the following command: 
~~~
python indic_transliterate.py --input <path to input file> --output <path to output file> --L1 <input language> --L2 <output language>
~~~
Lanugages should be in the 2-letter ISO 639-1 language code form. To see the list of supported languages, redirect to the ["IndicNLP page"](https://anoopkunchukuttan.github.io/indic_nlp_library/). Note that this script normalizes the input language text before transliterating, which we determined to not make a difference in inflectional models. 

## Romanization 
To get to the Romanization file follow the path: inflection_master/uroman-master/romanizer.py
To run the file, run the following command:
~~~
python romanizer.py --input <path to input file> --output <path to output file> --L1 <input language>
~~~
The language should in the 3-letter ISO 639-2 langauage code form. To see the list of supported languages, redirect to the URoman page. 

## IPA Transcription
To get to the IPA transcription file follow the path: inflection_master/epitran-master/convert_to_IPA.py
To run the file, run the following command:
~~~
python convert_to_IPA.py --input <path to input file> --output <path to output file> --L1 <input language>
~~~
The language should be in the form specified on the Epitran page. Redirect to that page as well for the supported languages.

## Evaluation
Using the 2019 SIGMORPHON Task 1 evaluation file, to evaluate the model outputs. Located in inflection_master/evalutate_2019_task1
To run the file, run the following command:
~~~
python evaluate_2019_task1.py --reference <path to gold file> --output <path to model output>
~~~

## Comparisons
To compare the output accuracies of 2 models, use the following file located at: inflection_master/compare.py
To run the file, run the following command:
~~~
python compare.py --test <path to experimental output file> --baseline <path to baseline output file> --gold <path to gold file> --output <path to output file>
~~~
The output file will contain the difference in the ratios of the instances when a morphological tag was included in a failed inflection. The higher the number the higher the improvements for this particular tag.

To compare the characters in 2 files for differences in normalization use the file located at: inflection_master/test_difference.py
To run the file, run the following command:
~~~
python test_difference.py --orig <path to non-normalized output> --norm <path to normalized output>
~~~

To use bootstrap evaluation statistical significance testing, use the code from https://github.com/neubig/util-scripts located in  inflection_master/paired_bootstrap.py
To run the file, run the following command:
~~~
python paired_bootstrap.py <path to gold file> <path to system 1 output> <path to system 2 output> 
~~~

## Citation
If you are using any of this code for your work, please cite the corresponding paper:
Nikitha Murikinati, Antonios Anastasopoulos, and Graham Neubig. 2020. Transliteration for cross-lingual morphological inflection. In Proc. SIGMORPHON. To appear.
