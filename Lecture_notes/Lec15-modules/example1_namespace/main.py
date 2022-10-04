import os, sys
os.system("cls||clear")

print(f"{'='*30}main.py{'='*30}")

# code imported from another module is excecuted when imported
import module1

# note __name__ is module1 when ran from outside of module1.py

print(f"main.py {__name__=}")

#when importing a module, a refence will be created to sys.modules
print("globals namespace")
print(globals()["module1"])

# when importing module1 it will be stored in sys.modules.
print("sys.modules")
print(sys.modules["module1"])

print(f"{'='*30}end_main{'='*30}")