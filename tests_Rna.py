import random
import unittest
from collections.abc import Hashable, Iterable, Iterator

from classes_hw import Dna, Rna


class DnaClassTests(unittest.TestCase):
    rc_dict = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

    @unittest.expectedFailure
    def test_init_uracil_in_seq(self):
        self.assertRaisesRegex(Exception,
                               'RNA sequence can not contain T',
                               Rna('ATGC'))
        self.assertRaisesRegex(Exception,
                               'RNA sequence can not contain T',
                               Rna('TTTT'))

    @unittest.expectedFailure
    def test_init_only_atgc_in_seq(self):
        self.assertRaisesRegex(Exception,
                               'Only A, U, G or C should be in RNA sequnce',
                               Rna('ABCD'))
        self.assertRaisesRegex(Exception,
                               'Only A, U, G or C should be in RNA sequnce',
                               Rna('0123'))

    @unittest.expectedFailure
    def test_init_empty_string(self):
        self.assertRaisesRegex(Exception,
                               'Sequence cannot be an empty string',
                               Rna(''))

    def test_init_normal_sequence(self):
        self.assertIsInstance(Rna('AUGCGCG'), Rna)

    def test_gc_content(self):
        test_cases = []
        for _ in range(100):
            case = ('AU' * random.randint(0, 1000) +
                    'GC' * random.randint(0, 1000))
            test_cases.append(case)
        for s in test_cases:
            with self.subTest(s):
                clue = (s.count('G') + s.count('C')) / len(s)
                self.assertEqual(Rna(s).gc_content(), clue)

    def test_reverse_complement(self):
        case = list('AU' * random.randint(1, 1000) +
                    'GC' * random.randint(1, 1000))
        random.shuffle(case)
        case = ''.join(case)
        clue = ''.join([self.rc_dict[i] for i in reversed(case)])
        self.assertEqual(Rna(case).reverse_complement(), clue)

    def test_iterator_type(self):
        case = 'A' * 100
        self.assertIsInstance(Rna(case), Iterator)
        self.assertIsInstance(Rna(case), Iterable)

    @unittest.expectedFailure
    def test_iterator_next(self):
        case = 'A' * 100
        self.assertRaises(StopIteration, next, Rna(case))

    def test_eq(self):
        case = 'A' * 100
        case2 = 'A' * 100
        case3 = 'C' * 100
        self.assertTrue(Rna(case) == Rna(case))
        self.assertTrue(Rna(case) == Rna(case2))
        self.assertFalse(Rna(case) == Rna(case3))

    def test_hash(self):
        case = 'A' * 100
        self.assertIsInstance(Rna(case), Hashable)

    def test_repr(self):
        case = 'A' * 100
        self.assertEqual(repr(Rna(case)), case)


if __name__ == '__main__':
    unittest.main(verbosity=2)
