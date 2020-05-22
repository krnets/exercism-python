# letter_values = {
#     1: "AEIOULNRST",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }

# def score(word):
# res = {v: k for k, v in letter_values.items()}
# return {letter_values[k]:k for k in letter_values}
# return letter_values
# return res

# def score(word):
#     res = {v: k for k, v in letter_values.items()}
#     return res

letter_values = dict(
    A=1, E=1, I=1, O=1, U=1, L=1, N=1, R=1, S=1, T=1,
    D=2, G=2,
    B=3, C=3, M=3, P=3,
    F=4, H=4, V=4, W=4, Y=4,
    K=5,
    J=8, X=8,
    Q=10, Z=10)


def score(word):
    return sum(letter_values[ch] for ch in word.upper())


q = score("at"), 2
q
q = score("zoo"), 12
q
q = score("street"), 6
q
