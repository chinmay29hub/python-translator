# Importing the library
from translate import Translator

# Specify the language to translate from
from_lang = 'Spanish'

# Specify the language to translate to 
to_lang = 'english'

# Passing the languages to the library
translator = Translator(from_lang, to_lang)

#printing the selected laguages
print(f"Currently the program will convert from{from_lang}----->{to_lang}\n\n")

# Asking the input
c = input("Enter the text to translate\n\n")

# Getting the translation
result = translator.translate(c)

# printing the translation
print("The translated text is:\n"+result)