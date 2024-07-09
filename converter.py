# Conversion factor from Hartree to eV
HARTREE_TO_EV = 27.2114

def convert_hartree_to_ev(hartree_energy):
    return hartree_energy * HARTREE_TO_EV

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            if line.strip() and not line.startswith('#'):
                parts = line.split()
                if len(parts) == 3:
                    num = parts[0]
                    occ = parts[1]
                    energy = float(parts[2])
                    energy_ev = convert_hartree_to_ev(energy)
                    outfile.write(f"{num:>7} {occ:>7} {energy_ev:>17.10f}\n")
                else:
                    outfile.write(line)
            else:
                outfile.write(line)

def main(input_file, output_file):
    process_file(input_file, output_file)

if __name__ == "__main__":
    input_file = 'hartree_energy.txt'  # Replace with your input file path
    output_file = 'converted_energy_ev.txt'  # Replace with your desired output file path
    main(input_file, output_file)
