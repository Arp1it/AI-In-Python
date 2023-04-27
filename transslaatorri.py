from translate import Translator

translator = Translator(to_lang='hindi')

translation = translator.translate("Hello, how are you? I'm fine, thanks.")

print(translation)