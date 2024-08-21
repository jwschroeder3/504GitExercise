import collections

def print_proportions(seq):
    """Print the proportions of each base in the string `seq`."""

    counts = collections.Counter(seq)
    total = counts.total()

    # It's printing proportions here, not frequencies, but we'll keep this label for
    # backwards compatibility.
    print('freqs')
    for base, n in counts.items():
        print(f'{base}:{n/total}')

print_proportions('ATCTGACGCGCGCCGC')
