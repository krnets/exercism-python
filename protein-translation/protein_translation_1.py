from itertools import takewhile

AMINO_ACIDS = {
    # Protein  :  Codon
    'Methionine':  ['AUG'],
    'Phenylalanine':  ['UUU', 'UUC'],
    'Leucine':  ['UUA', 'UUG'],
    'Serine':  ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine':  ['UAU', 'UAC'],
    'Cysteine':  ['UGU', 'UGC'],
    'Tryptophan':  ['UGG'],
    'STOP':  ['UAA', 'UAG', 'UGA']
}


def proteins(strand):
    codon_len = 3
    codons = [strand[i:i+codon_len]
              for i in range(0, len(strand)-codon_len+1, codon_len)]
    decoded = [k
               for c in codons
               for k, v in AMINO_ACIDS.items()
               if c in v]
    return list(takewhile(lambda x: x != 'STOP', decoded))


value = "AUG"
expected = ["Methionine"]

q = proteins(value), expected
q

value = "AUGUUUUGG"
expected = ["Methionine", "Phenylalanine", "Tryptophan"]
q = proteins(value), expected
q

value = "UAGUGG"
expected = []
q = proteins(value), expected
q

value = "UGGUAGUGG"
expected = ["Tryptophan"]
q = proteins(value), expected
q

value = "UGGUGUUAUUAAUGGUUU"
expected = ["Tryptophan", "Cysteine", "Tyrosine"]
q = proteins(value), expected
q
