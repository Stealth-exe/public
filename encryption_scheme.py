print("Hello World")
print("This will be a simple substitution cipher bet^n english alphabets and the some cyrillic characters.")

inp_raw_str= str(input("Your sentence:"))

substitution={'a':'а',
              'b':'б',
              'c':'в	',
              'd':'г',
              'e':'д',
              'f':'е',
              'g':'ё',
              'h':'ж',
              'i':'з',
              'j':'и',
              'k':'й',
              'l':'к',
              'm':'л',
              'n':'м',
              'o':'н',
              'p':'о',
              'q':'п',
              'r':'р',
              's':'с',
              't':'т',
              'u': 'у',
              'v':'ф',
              'w':'х',
              'x':'ц',
              'y':'ч',
              'z':'я',

              'A':'А',
              'B':'Б',
              'C':'В',
              'D':'Г',
              'E':'Д',
              'F':'Е',
              'G':'Ё',
              'H':'Ж',
              'I':'З',
              'J':'И',
              'K':'Й',
              'L':'К',
              'M':'Л',
              'N':'М',
              'O':'Н',
              'P':'О',
              'Q':'П',
              'R':'Р',
              'S':'С',
              'T':'Т',
              'U': 'У',
              'V':'Ф',
              'W':'Х',
              'X':'Ц',
              'Y':'Ч',
              'Z':'Я',

              '1':'0',
              '2':'9',
              '3':'8',
              '4':'7',
              '5':'6',
              '6':'5',
              '7':'4',
              '8':'3',
              '9':'2',
              '0':'1',


              '~':'~',
              '`': '`',
              '!': '!',
              '@': '@',
              '#': '#',
              '$': '$',
              '%': '%',
              '^': '^',
              '&': '&',
              '*': '*',
              '(': '(',
              ')': ')',
              '-': '-',
              '_': '_',
              '+': '+',
              '{': '{',
              '}': '}',
              '[': '[',
              ']': ']',
              '|': '|',
              '\\': '\\',
              ':': ':',
              ';': ';',
              '\'': '\'',
              '\"': '\"',
              '<': '<',
              '>': '>',
              '?': '?',
              '/': '/',
              ',': ',',
              '.': '.',}

if((input (str("enter 1 for encoding, any other character for decoding:")))=="1"):
    try:
        for i in inp_raw_str:
            if i in substitution:
                print(substitution[i],end='')
            else: print(i, end='')
    except Exception as e:
        print("wtf error")
else:
        substitution_swap = {v: k for k, v in substitution.items()}
        try:
            for k in inp_raw_str:
                if k in substitution_swap:
                    print(substitution_swap[k], end='')
                else:
                    print(k, end='')
        except Exception as e:
            print("wtf error")