import os, importlib

SOLUTIONS_DIR = "solutions" 

problems = [f for f in os.listdir(SOLUTIONS_DIR) if f.startswith('p_') and f.endswith('.py')]  

solutions = dict()

for file in problems:
    module = importlib.import_module(f"{SOLUTIONS_DIR}.{file[:-3]}")
    if hasattr(module, "template"): solutions[int(file[2:-3])] = module.template


def main():
    #print("Test:", solutions[12]("test.txt"))
    print(solutions[12]("../12.txt"))

if __name__ == '__main__':
    main() 
