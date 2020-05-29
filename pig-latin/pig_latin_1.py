import re

# if begins with a vowel sound, add an "ay" sound to the end of the word.
#     Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
# if begins with a consonant sound, move it to the end of the word
#     and then add an "ay" sound to the end of the word.
#     Consonant sounds can be made up of multiple consonants, a.k.a. a consonant cluster (e.g. "chair" -> "airchay").
# if starts with a consonant sound followed by "qu", move it to the end of the word,
#     and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
# if contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound
#     (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").


def translate(text):
    return ' '.join(pig_latin(word) for word in text.split())


def pig_latin(text):
    if re.match(r'^(xr|yt)', text):
        return text + 'ay'
    if re.match(r'^rh', text):
        return re.sub(r'^(rh)([aeiouy].+)', lambda m: m.group(2) + m.group(1) + 'ay', text)
    if re.match(r'^[^aeiou]+y', text):
        return re.sub(r'^([^aeiou])(y.*)', lambda m: m.group(2) + m.group(1) + 'ay', text)
    if re.match(r'^[^aeiou]*qu', text):
        return re.sub(r'^([^aeiou]*qu)([aeiou].+)', lambda m: m.group(2) + m.group(1) + 'ay', text)
    if re.match(r'^[^aeiou]', text):
        return re.sub(r'^([^aeiou]+)([aeiou].+)', lambda m: m.group(2) + m.group(1) + 'ay', text)
    if re.match(r'^[aeiou]', text):
        return text + 'ay'


q = translate("rhythm"), "ythmrhay"
q

q = translate("yttria"), "yttriaay"
q
q = translate("xray"), "xrayay"
q

q = translate("my"), "ymay"
q
q = translate("quick fast run"), "ickquay astfay unray"
q

q = translate("rhythm"), "ythmrhay"
q

q = translate("apple"), "appleay"
q
q = translate("ear"), "earay"
q
q = translate("igloo"), "iglooay"
q
q = translate("object"), "objectay"
q
q = translate("under"), "underay"
q
q = translate("equal"), "equalay"
q

q = translate("pig"), "igpay"
q
q = translate("koala"), "oalakay"
q
q = translate("xenon"), "enonxay"
q
q = translate("qat"), "atqay"
q
q = translate("chair"), "airchay"
q

q = translate("queen"), "eenquay"
q
q = translate("square"), "aresquay"
q

q = translate("therapy"), "erapythay"
q
q = translate("thrush"), "ushthray"
q
q = translate("school"), "oolschay"
q
q = translate("yellow"), "ellowyay"
q
