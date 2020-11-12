import os.path

ussr = []

def scan(stra):
    for stre in stra:
        if stre.isspace() or stre == "" or stre == None:
            pass
        else:
            if exec(stre) == None:
                ussr.append(stre)
            else:
                ussr.append(exec(stre))
    

def taker(fileZ):
    lignes = []
    if os.path.isfile(fileZ):
        with open(fileZ, "r") as f:
            for index, value in enumerate(f.readlines()):
                lignes.append(value.strip("\n"))
                lignes = [i for i in lignes if i] 
            scan(lignes)
        return ussr
    else:
        print("Uknown FILE")