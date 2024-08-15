import pytest
import numpy as np

import base_fraction

class TestBase:

    seq = 'ATCTGACGCGCGCCGC'
    bad_seq = 'ATCTGAC CGCGCCGC'
    valid_bases = ['A', 'C', 'T', 'G']

    def test_maxcount(self):
        '''Tests that the total count of bases equals the length of the
        input sequence.
        '''
        seq_len = 16
        # get the count of each base in self.seq as dictionary
        count_dict = base_fraction.count_bases(self.seq)
        # sum the values in the dictionary
        total_count = np.sum([count for count in count_dict.values()])
        # the count and length must be equal to pass this test
        assert total_count == seq_len

    def test_basecount(self):
        answer_dict={"A": 2, "C": 7, "G": 5, "T": 2}
        # get the count of each base in self.seq as dictionary
        count_dict = base_fraction.count_bases(self.seq)
        for base,base_count in answer_dict.items():
            assert base_count == count_dict[base]

    def test_base(self):
        '''Tests whether the set of characters in seq are in the allowable
        bases list.
        '''
        distinct_vals = set(self.seq)
        for val in distinct_vals:
            assert val in self.valid_bases

    def test_reject_base(self):
        '''Tests whether an Exception is raised when a forbidden cahracter
        appears masquerading as a base.
        '''
        # Check if NoSuchBaseException is raised
        with pytest.raises(base_fraction.NoSuchBaseException) as exc_info:
            base_fraction.check_seq(self.bad_seq)

        # Verify the exception was raised with the correct message
        assert exc_info.value.base == ' '
        assert exc_info.value.position == 7
        assert str(exc_info.value) == "Invalid base ' ' encountered at position 7"


