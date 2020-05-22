ALLERGENS = "eggs peanuts shellfish strawberries tomatoes chocolate pollen cats".split()


class Allergies:
    def __init__(self, score):
        self.score = list(map(int, reversed(f'{score % 256:b}'.zfill(8))))

    def allergic_to(self, item):
        return bool(self.score[ALLERGENS.index(item)])

    @property
    def lst(self):
        return [ALLERGENS[i] for i, x in enumerate(self.score) if x]
