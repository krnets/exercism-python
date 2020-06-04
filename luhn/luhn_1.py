import re


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if bool(re.findall(r'[\$\#\-a-z]', self.card_num)) or (len(self.card_num) <= 2 and '0' in self.card_num):
            return False
        aa = reversed(re.sub(r'\D', '', self.card_num))
        bb = list(map(int, aa))
        cc = [bb[i] * 2 if i % 2 else bb[i] for i in range(len(bb))]
        dd = [x-9 if x > 9 else x for x in cc]
        return sum(dd) % 10 == 0