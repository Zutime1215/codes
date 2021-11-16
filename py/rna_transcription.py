dna_seq = input("Paste Your DNA Sequence: ")
rna_seq = []

for i in dna_seq:
	
	if i == 'A':
		rna_seq.append('U')
	elif i == 'T':
		rna_seq.append('A')
	elif i == 'C':
		rna_seq.append('G')
	else:
		rna_seq.append('C')

rna_sequ = "".join(rna_seq) 	

print(f"RNA Transcript Sequence: {rna_sequ}")		

	