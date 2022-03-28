with open(input(), 'r') as f:
    result = f.read().split()

section_1 = result[0][0:result[0].find(result[1]) + 1]
section_2 = result[0][result[0].find(result[1]) + 1:]
section_3 = result[3][0] + ' ' + result[3][1:]
section_4 = result[4][0] + ' ' + result[4][1:]
original_GFP = section_1 \
               + result[2].replace(result[3], section_3, 1).replace(result[4], section_4, 1).split()[1] \
               + section_2

elements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
complementary_strand = ''.join([elements[i] for i in original_GFP])
print(original_GFP, complementary_strand, sep='\n')
