def slices(series, length):
    # if not series or length < 1 or length > len(series):
    if any([not series,  length < 1,  length > len(series)]):
        raise ValueError("invalid input")
    return [series[i:i+length] for i in range(len(series)-length+1)]


q = slices("1", 1), ["1"]
q
q = slices("12", 1), ["1", "2"]
q
q = slices("35", 2), ["35"]
q
q = slices("9142", 2), ["91", "14", "42"]
q
q = slices("777777", 3), ["777", "777", "777", "777"]
q
q = slices("918493904243", 5)
q
#      ["91849", "18493", "84939", "49390", "93904", "39042", "90424", "04243"]
