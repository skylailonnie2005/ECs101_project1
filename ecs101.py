import pandas as pd
x= "Hello World"

y=x.split(" ")

for item in y:
    for char in item:
        f = char.split()
        if char == "H":
            new = char.replace(f,0)
            print(new)
x= pd.read_csv



