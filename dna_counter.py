dna = input("Enter a DNA sequence: ")
dna = dna.upper()

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
