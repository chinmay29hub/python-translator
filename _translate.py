from translate import Translator

translator = Translator(from_lang = 'Spanish', to_lang = 'english')
print("Currently the program will convert from Spanish----->English\n\n")
c = input("Enter the text to translate\n\n")

result = translator.translate(c)


print("The translated text is "+result)
