from textwrap import wrap
from itertools import takewhile

AMINO_ACIDS = {
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
    codons = wrap(strand, 3)
    decoded = [k for c in codons for k, v in AMINO_ACIDS.items() if c in v]
    return list(takewhile(lambda x: x != 'STOP', decoded))
