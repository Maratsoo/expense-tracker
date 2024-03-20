#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

import json

expenses_file = open('expenses.json')
expenses = json.load(expenses_file) 
expenses_file.close() 

def sort_Summa(expense):
    return expense["Summa"]
        
# expenses = []

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    command = input("\nChoose command:")
    if command == "1":
        print(expenses)
        pass
    if command == "2":
        expenses.sort(key=sort_Summa, reverse=False)
        print(expenses[:10])
        pass
    if command == "3":
        expenses.sort(key=sort_Summa, reverse=True)
        print(expenses[:10])
        pass
    if command == "4":
        average_sum = (sum(expenses))/(len(expenses))
        print(average_sum)
        pass
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

