from num_dict import NUM_NOUN, NUM_ADJ

NUM_FORM = {
     'одно':'si',
     'один':'si',
     'два':'sr',
     'три':'sr',
     'четыре':'sr'
    }


def get_token_form(token):
    """
        Указыает в какую форму поставить токен после числа
        si - single imenitelny
        sr - single roditelny
        mr - many roditelny (по умолчанию)
    """

    if token in NUM_FORM.keys():
        return NUM_FORM[token]
    else:
        return 'mr'


def get_th(num, prev_number):
    """Определяет форму разрядов чисел - по позиции в тексте и"""
    num = num-2

    DICT_TH =  [
            {'si':'тысяча', 'sr':'тысячи','mr':'тысяч'},
            {'si':'миллион', 'sr':'миллиона','mr':'миллионов'},
            {'si':'миллиард', 'sr':'миллиарда','mr':'миллиардов'}
           ]

    if num >=0:
        return DICT_TH[num][get_token_form(prev_number)]
    else:
        return ''


def num2text_noun_part(input_num):
    """
        Перевод в текст чисел имеющие в составе не более трех цифр.
        Компонент функции num2text_noun(), которая мз таких троек собирает
        сколь угодно большие числа.
    """
    input_len = len(input_num)

    for j in range(input_len):
        a = input_num[j:]
        try:
            yield NUM_NOUN[a]
            break
        except:
            pass

    for i in range(input_len+1-j,input_len+1):
        x =  input_num[-i][0] + '0' * (i-1)
        try:
            yield NUM_NOUN[x]
        except:
            pass


def num2text_noun(input_num):
    """
        Перевод числа в текст - существительные
    """
    r = []
    input_num_l = format(int(input_num), ',').split(',')

    size = len(input_num_l)

    for i in input_num_l:

        t = list(num2text_noun_part(i))
        t.reverse()

        r = [*r,*t, get_th(size,  t[-1])]
        r = [i for i in r if len(i)]
        size -= 1

    r = ' '.join(r).strip()
    r = r.replace('один тыс','одна тыс').replace('два тыс','две тыс').split()

    return r
