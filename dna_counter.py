dna = input("Enter a DNA sequence: ")
dna = dna.upper()

valid = True
valid_bases = ["A", "T", "G", "C"]

for base in dna:
    if base not in valid_bases:
        print(base, "is not a valid DNA base.")
        valid = False
        break

if valid:
    a_count = dna.count("A")
    t_count = dna.count("T")
    g_count = dna.count("G")
    c_count = dna.count("C")

    gc_total = g_count + c_count
    dna_length = len(dna)
    gc_percentage = (gc_total / dna_length) * 100

    print("DNA analysis")
    print("------------")
    print("A:", a_count)
    print("T:", t_count)
    print("G:", g_count)
    print("C:", c_count)
    print(f"GC Content: {gc_percentage:.1f}%")

else:
    print("Invalid DNA sequence.")
    print("Please enter a sequence containing only A, T, G and C.")
