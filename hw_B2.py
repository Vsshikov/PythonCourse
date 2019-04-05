TrscrLib = {'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'}

DNA = input('Print DNA pls: \n')
RevComp = ''

for i, nuc in enumerate(DNA):
    RevComp = TrscrLib[nuc] + RevComp

print(RevComp)