import os, importlib

SOLUTIONS_DIR = "solutions" 

problems = [f for f in os.listdir(SOLUTIONS_DIR) if f.startswith('p_') and f.endswith('.py')]  

solutions = dict()

for file in problems:
    module = importlib.import_module(f"{SOLUTIONS_DIR}.{file[:-3]}")
    if hasattr(module, "template"): solutions[int(file[2:-3])] = module.template


def main():
    #print("Test:", solutions[14]("test.txt", 11, 7))
    print(solutions[14]("../14.txt", 101, 103))

if __name__ == '__main__':
    main() 
