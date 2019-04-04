gates = [
    "AND",
    "OR",
    "NOT",
    "NOR",
    "NAND",
    "XOR",
    "XNOR"
]

print("""
 ██▓     ▒█████    ▄████  ██▓ ▄████▄       ▄████  ▄▄▄     ▄▄▄█████▓▓█████   ██████ 
▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒▒██▀ ▀█      ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ ▒██    ▒ 
▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▒▓█    ▄    ▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   ░ ▓██▄   
▒██░    ▒██   ██░░▓█  ██▓░██░▒▓▓▄ ▄██▒   ░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄   ▒   ██▒
░██████▒░ ████▓▒░░▒▓███▀▒░██░▒ ▓███▀ ░   ░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒▒██████▒▒
░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ░▒ ▒  ░    ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░
░ ░ ▒  ░  ░ ▒ ▒░   ░   ░  ▒ ░  ░  ▒        ░   ░   ▒   ▒▒ ░   ░     ░ ░  ░░ ░▒  ░ ░
  ░ ░   ░ ░ ░ ▒  ░ ░   ░  ▒ ░░           ░ ░   ░   ░   ▒    ░         ░   ░  ░  ░  
    ░  ░    ░ ░        ░  ░  ░ ░               ░       ░  ░           ░  ░      ░  
                             ░                                                     
                                +PLEASE TYPE IN CAPS+                                
""")


choice = input("Gate> ")
if choice == gates[0]:
    print("AND TRUTH TABLE")
    print("| A | B | Z |\n| 0 | 0 | 0 |\n| 0 | 1 | 0 |\n| 1 | 0 | 0 |\n| 1 | 1 | 1 |")
elif choice == gates[1]:
    print("OR TRUTH TABLE")
    print("| A | B | Z |\n| 0 | 0 | 0 |\n| 0 | 1 | 1 |\n| 1 | 0 | 1 |\n| 1 | 1 | 1 |")
elif choice == gates[2]:
    print("NOT TRUTH TABLE")
    print("| A | Z |\n| 0 | 1 |\n| 1 | 0 |")
elif choice == gates[3]:
    print("NOR TRUTH TABLE")
    print("| A | B | Z |\n| 0 | 0 | 1 |\n| 0 | 1 | 0 |\n| 1 | 0 | 0 |\n| 1 | 1 | 0 |")
elif choice == gates[4]:
    print("NAND TRUTH TABLE")
    print("| A | B | Z |\n| 0 | 0 | 1 |\n| 0 | 1 | 1 |\n| 1 | 0 | 1 |\n| 1 | 1 | 0 |")
elif choice == gates[5]:
    print("XOR TRUTH TABLE")
    print("| A | B | Z |\n| 0 | 0 | 0 |\n| 0 | 1 | 1 |\n| 1 | 0 | 1 |\n| 1 | 1 | 0 |")
elif choice == gates[6]:
    print("XNOR TRUTH TABLE")
    print("| A | B | Z |\n| 0 | 0 | 1 |\n| 0 | 1 | 0 |\n| 1 | 1 | 0 |\n| 1 | 1 | 0 |")
elif choice == 'q':
    quit()
else:
    print("Invalid Option!")
    quit()