
example = "dabAcCaCBAcCcaDA"

    
def react(molecule):
    new_molecule = ""
    last = ""
    for atom in molecule:
        opposite_polarity = atom.isupper() ^ last.isupper()
        same_atom = atom.upper() == last.upper()
        if same_atom and opposite_polarity:
            new_molecule = new_molecule[0:-1]  # new_molecule.pop()
            last = new_molecule[-1] if new_molecule else ""
            continue
        new_molecule += atom
        last = atom
    return new_molecule


print("part 1:", len(react(open('day5.txt').read())))

def reacted_len(molecule):
    return len(react(molecule))

def remove(molecule, atom):
    return molecule.replace(atom.lower(), "").replace(atom.upper(), "")

def key(molecule):
    def inner(atom):
        return reacted_len(remove(molecule, atom))
    return inner

reagent = open('day5.txt').read()
print("part 2:", min(map(key(reagent), sorted(set(reagent.lower())))))