def transliteration(word):
    translited = ""
    capTrans = {'А': 'A',
                'Б': 'B',
                'В': 'V',
                'Г': 'H',
                'Ґ': 'G',
                'Д': 'D',
                'Е': 'E',
                'Ё': 'E',
                'Є': 'Ye',
                'Ж': 'Zh',
                'З': 'Z',
                'И': 'Y',
                'Ї': 'Yi',
                'Й': 'Y',
                'К': 'K',
                'Л': 'L',
                'М': 'M',
                'Н': 'N',
                'О': 'O',
                'П': 'P',
                'Р': 'R',
                'С': 'S',
                'Т': 'T',
                'У': 'U',
                'Ф': 'F',
                'Х': 'Kh',
                'Ц': 'Ts',
                'Ч': 'Ch',
                'Ш': 'Sh',
                'Щ': 'Shch',
                'Ъ': '',
                'Ы': 'Y',
                'Ь': '',
                'Э': 'E',
                'Ю': 'Yu',
                'Я': 'Ya'}
    lowerTrans = {'а': 'a',
                          'б': 'b',
                          'в': 'v',
                          'г': 'h',
                          'ґ': 'g',
                          'д': 'd',
                          'е': 'e',
                          'є': 'ye',
                          'ё': 'e',
                          'ж': 'zh',
                          'з': 'z',
                          'и': 'y',
                          'і': 'i',
                          'ї': 'yi',
                          'й': 'y',
                          'к': 'k',
                          'л': 'l',
                          'м': 'm',
                          'н': 'n',
                          'о': 'o',
                          'п': 'p',
                          'р': 'r',
                          'с': 's',
                          'т': 't',
                          'у': '',
                          'ф': 'f',
                          'х': 'kh',
                          'ц': 'ts',
                          'ч': 'ch',
                          'ш': 'sh',
                          'щ': 'shch',
                          'ъ': '',
                          'ы': 'y',
                          'ь': '',
                          'э': 'e',
                          'ю': 'yu',
                          'я': 'ya'}
    for i, char in enumerate(word):
        if char in capTrans:
            char = capTrans[char]
            if len(word) > i+1:
                if word[i+1] not in lowerTrans:
                    char = char.upper()
            else:
                char = char.upper()
        elif char in lowerTrans:
            char = lowerTrans[char]
        elif not(48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or char == '.'):
            char = "_"
        translited += char
    return translited
                