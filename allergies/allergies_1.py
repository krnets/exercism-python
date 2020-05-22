ALLERGENS = "eggs peanuts shellfish strawberries tomatoes chocolate pollen cats".split()


class Allergies:
    def __init__(self, score):
        self.score = list(map(int, reversed(f'{score % 256:b}'.zfill(8))))

    def allergic_to(self, item):
        return bool(self.score[ALLERGENS.index(item)])

    @property
    def lst(self):
        return [ALLERGENS[i] for i, x in enumerate(self.score) if x]


a = Allergies(8)
q = a.score
q
# q = a.allergies
q
q = Allergies(0).allergic_to("eggs"), False
q
q = Allergies(1).allergic_to("eggs"), True
q
# q = [int(x) for x in bin(64)[2:].zfill(8)[::-1]]
# q
q = Allergies(255).lst
q
# [ "eggs","peanuts","shellfish","strawberries","tomatoes","chocolate","pollen","cats",],

q = Allergies(509).lst
q
# ["eggs","shellfish","strawberries","tomatoes","chocolate","pollen","cats"],x
