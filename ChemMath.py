"""ChemMath.py: Assistant for basic chemistry mathematics. Intended to eventually support graphing calculators"""

__author__ = "Russ Johnson"
__version__ = "0.9.1"
__status__ = "in development"

import re

atomic_masses = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011, 'N': 14.007,
    'O': 15.999, 'F': 18.998, 'Ne': 20.180, 'Na': 22.990, 'Mg': 24.305, 'Al': 26.982,
    'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
    'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933,
    'Ni': 58.693, 'Cu': 63.546, 'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.63, 'As': 74.922, 'Se': 78.971,
    'Br': 79.904, 'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906}


def main_menu_ui():
    print("Select a category:")
    print("1: Molar Mass")
    print("2: Balance Reaction Equations")
    return input("Enter choice ")


def molar_mass_ui():
    valid_choices = ['1', '2', '3']
    response = ""
    while (response not in valid_choices):
        print("Select a category:")
        print("1: Molar Mass")
        print("2: Balance Reaction Equations")
        print("3: Something else")
        response = input("Enter choice ")
        print(response)
    return response


def main_menu():
    stop_program = False
    while (not stop_program):
        match main_menu_ui():
            case '1':
                print("Molar Mass")
                molar_mass()
            case '2':
                print("Balance Reaction Equations")
            case '3':
                print("Something else")
            case '0':
                stop_program = True
        #case _:
        #    main_menu()


def molar_mass():
    print("Molar Mass. Enter the ")
    break_down_formula("H2SO4")


'''Input a molecular formula returns a dictionary of the element and thier counts'''


def break_down_formula(formula):
    # TODO: Only supports 1 level of parenthesis
    # TODO: Only supports 2 digit coefficients
    element_counts = {}
    splits = []
    # first, break down any parenthesis
    if '(' in formula:
        splits = re.split(r'[()]', formula)
        # look for any multiplies that are associated with in-parenthesis
        for i, sub_string in enumerate(splits):
            # if the substring starts with a number, that number is a multiple for the previous sub string
            if sub_string[0].isnumeric() and i > 0:  # don't run on the 1st substring
                value = 0
                # identify the number
                if len(sub_string) == 1:  # if there is only one character it must be a single digit number
                    value = int(sub_string)
                else:  # it may be a 2 digit number
                    # check for 2 digit number
                    if sub_string[1].isnumeric():
                        value = int(sub_string[0:1])
                    else:
                        value = int(sub_string[0])
                # add extra copies of what was in the parenthesis to account for the parentheses coefficient
                for x in range(value - 1): splits.append(
                    splits[i - 1])  # -1 because the original in the parentheses still counts
        # create a new list to hold the elements without leading coefficients
        elements = []
        # strip out any leading numbers
        for split in splits:
            if len(split) == 1:
                if not split[0].isnumeric():
                    elements.append(split)
            else:
                if not split[0].isnumeric():
                    elements.append(split)
                #check for 2 digit number
                elif split[1].isnumeric():
                    #if both leading characters are digits
                    if split[0].isnumeric():
                        elements.append(split[2:])
                    else:
                        elements.append(split)
                #if only 1st charcater is a digit
                elif split[0].isnumeric():
                    elements.append(split[1:])
        formula = "".join(elements)
    # parentheses are now removed
    element_counts = {}
    # Spits the molecular formula into a list of strings. Uses uppercase letters to know where to divide the string.
    element_strings = re.findall('[A-Z][^A-Z]*', formula)
    for element in element_strings:
        # splits the substring into a string of the letters (Atomic Symbol) and number (amount of atoms)
        #  also discards any empty strings
        element_split = [part for part in re.split(r'(\d+)', element) if part != '']
        # if there is no number associdated with the element, give it a count of '1'
        if len(element_split) == 1: element_split.append('1')
        # add the element to the dictionary and add the count to that key's value
        if element_split[0] in element_counts:
            element_counts[element_split[0]] += int(element_split[1])
        else:
            element_counts[element_split[0]] = int(element_split[1])
    return element_counts


def break_down_formula_old(formula):
    # TODO: Only supports 1 level of parenthesis
    element_counts = {}
    # Cu(NO3)2
    #first, break down any parenthesis
    if '(' in formula:
        open_indices = [match.start() for match in re.finditer(r'\(', formula)]
        close_indices = [match.start() for match in re.finditer(r'\)', formula)]
        for i, index in enumerate(open_indices):
            #look after parenthesis to see if there is a muliplier
            pass
        pass
    else:
        pass

    # Spits the molecular formula into a list of strings. Uses uppercase letters to know where to divide the string.
    element_strings = re.findall('[A-Z][^A-Z]*', formula)
    print(element_strings)
    for element in element_strings:
        # splits the substring into a string of the letters (Atomic Symbol) and number (amount of atoms)
        #  also discards any empty strings
        element_split = [part for part in re.split(r'(\d+)', element) if part != '']
        # if there is no number associdated with the element, give it a count of '1'
        if len(element_split) == 1: element_split.append('1')
        # add the element to the dictionary and add the count to that key's value
        if element_split[0] in element_counts:
            element_counts[element_split[0]] += int(element_split[1])
        else:
            element_counts[element_split[0]] = int(element_split[1])
    return element_counts


def element_masses(element_dict):
    total_mass = 0
    for element in element_dict:
        #look up the mass of the element and add the mass * the count to the mass total
        total_mass += atomic_masses[element] * element_dict[element]
    return total_mass


#main_menu()
print(break_down_formula("Cu(NO3)2H2O"))
print(element_masses(break_down_formula("Cu(NO3)2H2O")))
