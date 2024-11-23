import unicodedata

def normalizar_texto(texto):
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn'
                )
    texto = ''.join(c for c in texto if c.isalnum() or c.isspace())
    texto = ' '.join(texto.split())

    return texto.strip()