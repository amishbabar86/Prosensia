def greet(lang_code):
    if lang_code == 'en':
        print("Hello")
    elif lang_code == 'es':
        print("Hola")
    elif lang_code == 'fr':
        print("Bonjour")
    else:
        print("Language code not recognized")

# Testing the function with each language code
greet('en')
greet('es')
greet('fr')
