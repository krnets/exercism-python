import re

def parse(markdown):
    res = ''
    in_list = False
    in_list_append = False
    for i in markdown.splitlines():
        if bool(re.match('###### (.*)', i)):
            i = '<h6>' + i[7:] + '</h6>'
        elif bool(re.match('## (.*)', i)):
            i = '<h2>' + i[3:] + '</h2>'
        elif bool(re.match('# (.*)', i)):
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res

# import re


# def parse(markdown):
#     res = []
#     for line in markdown.split('\n'):
#         line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)
#         line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)

#         header_match = re.match(r'(#+) (.*)', line)
#         if header_match:
#             res.append('<h{0}>{1}</h{0}>'.format(
#                 len(header_match.group(1)), header_match.group(2)))
#         elif line.startswith('* '):
#             if res and res[-1] == '</ul>':
#                 res.pop()
#             else:
#                 res.append('<ul>')
#             res.append('<li>' + line[2:] + '</li>')
#             res.append('</ul>')
#         else:
#             res.append('<p>' + line + '</p>')
#     return ''.join(res)    
#     # return 1