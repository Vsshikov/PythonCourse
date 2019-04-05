SeqFile = open('rosalind_hamm.txt')

Seq1 = SeqFile.readline()
Seq2 = SeqFile.readline()

Seq1.replace(' ', '')
Seq1.replace('\n', '')
Seq2.replace(' ', '')
Seq2.replace('\n', '')

HamDist = 0

for i, nuc in enumerate(Seq1):
    if nuc != Seq2[i]:
        HamDist += 1

print('Hamming distance: {}'.format(HamDist))