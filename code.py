'''Simple utilites for counting and reporting the fraction of positions
in a sequence that belong to each base.
'''

def count_basie(seq):
    '''Counts the number of occurances of each base in seq. Returns
    a dictionary, the keys of which are bases and the values of which
    are the frequency of each base.

    Args:
    -----
    seq : str
        The sequence in which to count base occurances.

    Returns:
    --------
    base_count_dict : dict
        A dictionary, the keys of which are base identities,
        the values of which are the number of occurences of the key base.
    '''

    base_count_dict = dict()
    for base in seq:
        if base not in base_count_dict:
            base_count_dict[base] = 1
        else:
            base_count_dict[base] += 1
    return base_count_dict

def print_base_fractions(count_dict):
    '''Prints the proportion of positions having each base in
    the input dictionary.

    Args:
    -----
    count_dict : dict
        Dictionary, the keys of which are base identities,
        the values of which are the number of occurences of the base.

    Returns:
    --------
    None

    Prints:
    -------
    Fraction of bases counted in count_dict belonging to each base.
    '''

    print()
    print('Fraction of bases of each identity in sequence')
    print("----------------------------------------------")
    total = float(sum([count_dict[base] for base in count_dict.keys()]))
    for base in count_dict.keys():
        base_frac = count_dict[base] / total
        print(base + ': ' + str(base_frac))

if __name__ == "__main__":
    base_counts = count_basie('ATCTGACGCGCGCCGC')
    print_base_fractions(base_counts)

