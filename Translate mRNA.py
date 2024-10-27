'''
Task2: Translate a given mRNA sequence (with Uracil bases instead of Thymine)
to its amino acid sequence.
Author: Dinuri Lokuwalpola
date: 25/11/2022
'''
# Read the codon table
diction={}
with open ("codon_table.txt", 'r') as file1:

    # create a dictionary to store codon-amino acid mapping
    for line in file1:
        if "#" not in line:
            newline = line.strip().split()
            codon = newline[0]
            AminoA = newline[2]
            diction[codon] = AminoA
print(diction)

# read the mRNA sequence
with open ("OSDREB1A_mRNA.fasta", 'r') as file2:
    for line2 in file2:
        lines = line2.strip()
        if lines != '\n':
            if ">" not in lines:
                # split mRNA-sequence into codons(3 bases) and store in an array
                arr = []
                for i in range (0, len(lines),3):
                    c = (lines[i:i+3])
                    arr.append(c)
print(arr)

# translate codons of mRNA sequence to its amino acid
aa =""
num=0
while num < len(arr):
    c = arr[num]
    aa += diction.get(c)
    if c in ["UAA","UAG","UGA"]:
        break
    num += 1

#create a file & write the sequence
f = open("Amino_Acid.fasta", "w")
f.write(">OSDREB1A_amino acid.fasta\n" + aa)
print(aa)

#get the length of translated amino acid sequence
print(len(aa))






















