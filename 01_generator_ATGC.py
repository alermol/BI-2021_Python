import itertools


def generate(n: int):
    for i in range(1, n + 1):
        for seq in itertools.product('ATGC', repeat=i):
            yield ''.join(seq)
