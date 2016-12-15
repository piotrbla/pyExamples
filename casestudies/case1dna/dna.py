def main():
    input_file_name = "dna.txt"
    f = open(input_file_name, "r")
    seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")

if __name__ == '__main__':
    main()
