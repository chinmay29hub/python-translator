from translate import Translator

translator = Translator(from_lang = 'Spanish', to_lang = 'english')

result = translator.translate('Hola codificadora')


print("The translated text is "+result)
