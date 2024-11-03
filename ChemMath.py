
"""ChemMath.py: Assistant for basic chemistry mathematics. Intended to eventually support graphing calculators"""

__author__  = "Russ Johnson"
__version__ = "0.9.1"
__status__  = "in development"

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
    while(response not in valid_choices):
        print("Select a category:")
        print("1: Molar Mass")
        print("2: Balance Reaction Equations")
        print("3: Something else")
        response = input("Enter choice ")
        print(response)
    return response

def main_menu():
    stop_program = False
    while(not stop_program):
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
    element_counts = {}
    element_counts['H'] = 1
    print(f"{element_counts['H']=}")
    pass



main_menu()