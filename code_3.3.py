import requests
import os


def translate_it(in_file, out_file, in_language, out_language='ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': '{}-{}'.format(in_language, out_language),
        'text': open(in_file, 'r').read(),
    }
    response = requests.get(url, params=params).json()
    with open(out_file, 'w') as f:
        f.write(response['text'][0])


def main():
    source = 'source'
    result = 'result'
    if not os.path.exists(result):
        os.mkdir(result)

    for in_file in os.listdir(source):
        translate_it(os.path.join(source, in_file), os.path.join(result, in_file), in_file.replace('.txt', '').lower())


if __name__ == '__main__':
    main()
