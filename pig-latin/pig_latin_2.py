import re


def translate(text):
    return ' '.join(pig_latin(word) for word in text.split())


def pig_latin(text):
    if re.match(r'^(xr|yt)', text):
        return text + 'ay'
    elif re.match(r'^rh', text):
        return re.sub(r'^(rh)([aeiouy].+)', swap_add_ay, text)
    elif re.match(r'^[^aeiou]+y', text):
        return re.sub(r'^([^aeiou])(y.*)', swap_add_ay, text)
    elif re.match(r'^[^aeiou]*qu', text):
        return re.sub(r'^([^aeiou]*qu)([aeiou].+)', swap_add_ay, text)
    elif re.match(r'^[^aeiou]', text):
        return re.sub(r'^([^aeiou]+)([aeiou].+)', swap_add_ay, text)
    return text + 'ay'


def swap_add_ay(m):
    return m.group(2) + m.group(1) + 'ay'
