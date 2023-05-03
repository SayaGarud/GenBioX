from GenBioX import data_preprocessing

#--------------------------------------------------------------------------#
# Function 1 - Read_Fasta

sequences = data_preprocessing.read_fasta("test.fasta.txt")

# Print the sequences
for seq_id, seq in sequences.items():
    print(seq_id, seq)
    
#--------------------------------------------------------------------------#
# Function 2 - Fetch_Seq

seq = data_preprocessing.fetch_seq('Nucleotide', 'NM_000525.5')
