class Dna:

    def __init__(self, seq: str):
        self.seq = seq.upper()
        if 'U' in self.seq:
            raise Exception("DNA sequence can not contain U")
        elif not set(self.seq).issubset(set('ATGC')):
            raise Exception('Only A, T, G or C should be in DNA sequnce')

    def gc_content(self):
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq)

    def reverse_complement(self):
        rc_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join([rc_dict[i] for i in reversed(self.seq)])

    def transcribe(self):
        transcr_dict = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
        return Rna(''.join([transcr_dict[i] for i in self.seq]))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.seq):
            self.n += 1
            return self.seq[self.n - 1]
        else:
            raise StopIteration

    def __eq__(self, other):
        return self.seq == other.seq

    def __hash__(self):
        return hash(self.seq)


class Rna():

    def __init__(self, seq: str):
        self.seq = seq.upper()
        if 'T' in self.seq:
            raise Exception("RNA sequence can not contain T")
        elif not set(self.seq).issubset(set('AUGC')):
            raise Exception('Only A, U, G or C should be in RNA sequnce')

    def gc_content(self):
        return (self.seq.count('G') + self.seq.count('C')) / len(self.seq)

    def reverse_complement(self):
        rc_dict = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
        return ''.join([rc_dict[i] for i in reversed(self.seq)])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.seq):
            self.n += 1
            return self.seq[self.n - 1]
        else:
            raise StopIteration

    def __eq__(self, other):
        return self.seq == other.seq

    def __hash__(self):
        return hash(self.seq)

    def __repr__(self):
        return str(self.seq)
