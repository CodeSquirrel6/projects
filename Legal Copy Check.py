legal_copy = input("Paste confirmed legal copy: ")
check_legal = input("Paste legal copy to check: ")

if legal_copy == check_legal:
    print("Legal copy is correct.")
else:
    print("Legal copy DOES NOT match.")