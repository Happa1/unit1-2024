#Aug_28

"""Quiz003"""
in_protein=str(input("please input alphabet"))
def DNAtranslator(in_protein: str):
    out_protein = ''
    if in_protein=='A':
        out_protein='T'
    elif in_protein=='G':
        out_protein='C'
    elif in_protein=='T':
        out_protein='A'
    elif in_protein=='C':
        out_protein='G'
    else:
        print("invalid")
    return out_protein

out_protein=DNAtranslator(in_protein)
print(out_protein)

"""Quiz003 HL"""
in_protein=str(input("please input alphabet"))
def DNAtranslator(in_protein: str) ->str:
    out_protein = ''
    for char in in_protein:
        if char == 'A':
            out_protein += 'T'
        elif char == 'G':
            out_protein += 'C'
        elif char == 'T':
            out_protein += 'A'
        elif char == 'C':
            out_protein += 'G'
        else:
            print("invalid")

    return out_protein

test = DNAtranslator(in_protein)
print(test)


"""reverse word"""
def mystery_box1(word:str, flip_case:bool) ->str:
    "this function revreses the word"
    output = ""
    for letter in word:
        output=letter + output

    if flip_case==True:
        output= output.lower()
    return output

#calling the function
test=mystery_box1(word="Hello", flip_case=True)
print(test)

"""email"""
def mystery_box2(email:str):
    username, domain = email.split('@')
    username_to_remove = "."
    modified_username = username.replace(username_to_remove, " ")
    username_return = modified_username.title()

    return username_return, domain


test=mystery_box2(email="John.doe@gmail.com")
print(test)

