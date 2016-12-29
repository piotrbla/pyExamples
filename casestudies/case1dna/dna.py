def decode_dna_sequence(sequence):
    """
    Translates dna sequence into amino acids string, you should find CDS (last 3 characters is stop codon
    :param sequence: dna sequence to translate
    :return: decoded protein (amino acids) sequence
    """
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    decoded_protein = ""
    if len(sequence) % 3:
        raise Exception("Wrong dna sequence, length should be a multiple of 3")
    for i in range(0, len(sequence), 3):
        dna_codon = sequence[i:i + 3]
        # print(dna_codon)
        # print(table[dna_codon])
        decoded_protein += table[dna_codon]
    return decoded_protein


def read_sequence(input_file_name):
    """Reads and returns input sequence with special characters removed"""
    with open(input_file_name, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq


def cipher():
    import string
    string.ascii_lowercase

    # We will consider the alphabet to be these letters, along with a space.
    alphabet = string.ascii_lowercase + " "

    letters = dict()
    i = 0
    for x in alphabet:
        letters[x] = i
        i += 1
    print(letters)

    alphabet = string.ascii_lowercase + " "
    letters = dict(enumerate(alphabet))


def caesar_cipher():
    import string
    alphabet = string.ascii_lowercase + " "
    letters = dict(enumerate(alphabet))
    key = 3
    message = "hi my name is caesar"
    code = {}
    for k, v in letters.items():
        code[v] = (k + key) % len(alphabet)

    coded_message = ""
    for letter in message:
        coded_message += letters[code[letter]]
    print(coded_message)


def main():
    caesar_cipher()
    input_file_name = "dna.txt"
    # seq = read_sequence(input_file_name)
    # print(seq[40:50])
    # # print(len(seq))
    # # help(decode_dna_sequence)
    # print(decode_dna_sequence(seq[20:938])[:-1])
    # print(decode_dna_sequence(seq[20:935]))
    # print(decode_dna_sequence(seq[20:938])[:-1] == decode_dna_sequence(seq[20:935]))
    # Let's look at the lowercase letters.


if __name__ == '__main__':
    main()
