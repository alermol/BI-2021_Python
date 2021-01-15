import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO

path_to_fasta = 'sample.fasta'

record_dict = SeqIO.to_dict(SeqIO.parse(path_to_fasta, 'fasta'))
lengths = np.array([len(record.seq) for record in record_dict.values()])
counts, bins = np.histogram(lengths, bins=200)
plt.hist(bins[:-1], bins, weights=counts, color='green')
plt.xlim(0, 4000)
plt.grid(alpha=0.3)
plt.xlabel('Sequence length, bp')
plt.ylabel('Number')
plt.title('Frequency distribution of sequences lenghts in FASTA file')
plt.savefig('02_fasta_freq.jpeg', bbox_inches='tight')
