import random
import unittest
from collections.abc import Hashable, Iterable, Iterator

from classes_hw import Dna, Rna


class DnaClassTests(unittest.TestCase):
    rc_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    transcr_dict = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

    @unittest.expectedFailure
    def test_init_uracil_in_seq(self):
        self.assertRaisesRegex(Exception,
                               'DNA sequence can not contain U',
                               Dna('ATUC'))
        self.assertRaisesRegex(Exception,
                               'DNA sequence can not contain U',
                               Dna('UUUU'))

    @unittest.expectedFailure
    def test_init_only_atgc_in_seq(self):
        self.assertRaisesRegex(Exception,
                               'Only A, T, G or C should be in DNA sequnce',
                               Dna('ABCD'))
        self.assertRaisesRegex(Exception,
                               'Only A, T, G or C should be in DNA sequnce',
                               Dna('0123'))

    @unittest.expectedFailure
    def test_init_empty_string(self):
        self.assertRaisesRegex(Exception,
                               'Sequence cannot be an empty string',
                               Dna(''))

    def test_init_normal_sequence(self):
        self.assertIsInstance(Dna('ATGCGCG'), Dna)

    def test_gc_content(self):
        case1 = 'AT' * 10 + 'GC' * 40
        case2 = 'GC' * 50
        case3 = 'AT' * 50
        self.assertEqual(Dna(case1).gc_content(), 0.8)
        self.assertEqual(Dna(case2).gc_content(), 1.0)
        self.assertEqual(Dna(case3).gc_content(), 0.0)

    def test_reverse_complement(self):
        case = list('AT' * random.randint(1, 1000) +
                    'GC' * random.randint(1, 1000))
        random.shuffle(case)
        case = ''.join(case)
        clue = ''.join([self.rc_dict[i] for i in reversed(case)])
        self.assertEqual(Dna(case).reverse_complement(), clue)

    def test_transcribe(self):
        case = list('AT' * random.randint(1, 1000) +
                    'GC' * random.randint(1, 1000))
        random.shuffle(case)
        case = ''.join(case)
        clue = ''.join([self.transcr_dict[i] for i in case])
        self.assertIsInstance(Dna(case).transcribe(), Rna)
        self.assertEqual(Dna(case).transcribe(), Rna(clue))

    def test_iterator_type(self):
        case = 'A' * 100
        self.assertIsInstance(Dna(case), Iterator)
        self.assertIsInstance(Dna(case), Iterable)

    @unittest.expectedFailure
    def test_iterator_next(self):
        case = 'A' * 100
        self.assertRaises(StopIteration, next, Dna(case))

    def test_eq(self):
        case = 'A' * 100
        case2 = 'A' * 100
        case3 = 'C' * 100
        self.assertTrue(Dna(case) == Dna(case))
        self.assertTrue(Dna(case) == Dna(case2))
        self.assertFalse(Dna(case) == Dna(case3))

    def test_hash(self):
        case = 'A' * 100
        self.assertIsInstance(Dna(case), Hashable)


if __name__ == '__main__':
    unittest.main(verbosity=2)
