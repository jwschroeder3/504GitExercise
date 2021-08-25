def function1(a):
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def freq_count(sequence):
    print('freqs')
    total = float(sum([sequence[base] for base in sequence.keys()]))
    for base in sequence.keys():
        print(base + ':' + str(sequence[base]/total))

freq_count(function1('ATCTGACGCGCGCCGC'))
