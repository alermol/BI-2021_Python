import itertools

from Bio import SeqIO
from Bio.Seq import Seq


def translate(fasta, codon_table='Standard'):
    records_list = SeqIO.index(fasta, 'fasta')
    for record in records_list.values():
        yield record.translate(table=codon_table)
