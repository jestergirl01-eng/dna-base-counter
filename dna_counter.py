dna = input("Enter a DNA sequence: ")
dna = dna.upper()

a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print("DNA analysis")
print("------------")
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
