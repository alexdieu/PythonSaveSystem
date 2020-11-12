def save(value, file, mode):
    if mode == 1 or mode == '0':
        with open(file, "a") as s:
            s.write("\n" + str(value) + "\n")
            s.close()
    if mode == 0 or mode == '0':
        with open(file, "w") as s :
            s.write(str(value) + "\n")
            s.close()
    else:
        print("ModERROR : Uknown Mod : %s ! Help: 0 for new file and 1 for continue writing" % mode)