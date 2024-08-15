BASES = ["A", "C", "G", "T"]


class NoSuchBaseException(Exception):
    '''Class used to raise helpful Exception when invalid base is encountered
    '''

    def __init__(self, bad_base, position):
        self.base = bad_base
        self.position = position
        self.message = f"Invalid base '{self.base}' encountered at position {self.position}"
        super().__init__(self.message)


def check_seq(seq):
    '''QC helper to check input sequence for invalid bases.
    If any character is encountered which is not in BASES,
    raise NoSuchBaseException.
    '''
    for i,char in enumerate(seq):
        if char not in BASES:
            raise NoSuchBaseException(char, i)


def count_bases(seq):
    '''Counts the number of occurances of each base in seq.

    Args:
    -----
    seq : str
        The sequence to count base occurances in

    Returns:
    --------
    base_count_dict : dict
        Dictionary, the keys of which are base identities,
        the values of which are the number of occurences of the base.
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

    print('freqs')
    total = float(sum([count_dict[base] for base in count_dict.keys()]))
    for base in count_dict.keys():
        print(base + ':' + str(count_dict[base]/total))

if __name__ == "__main__":
    seq = 'ATCTGACGCGCGCCGC'
    check_seq(seq)
    base_counts = count_bases(seq)
    print_base_fractions(base_counts)
