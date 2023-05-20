import random
import string

def generate_password():

    #select one capital letter 
    capital_letter = random.choice(string.ascii_uppercase)

    #select two special characters
    special_char = random.sample(string.punctuation,2)

    #select remaining alphanumeric chars
    alphanumeric = string.ascii_letters + string.digits
    rem_chars = ''.join(random.choice(alphanumeric)for x in range(5) )

    #structure all selected chars to get password
    password = capital_letter + special_char[0] + special_char[1] + rem_chars

    #shuffling the password to ensure randomness
    password_lst = list(password)
    random.shuffle(password_lst)
    password = ''.join(password_lst)

    return password

#creating reference obj for generate func to be callable
passd = generate_password()

#identifing the password to which it is being used
identify = input("Enter the identification of these password to which it is being used : ")

#saving generated password locally
file_path = f"{identify}.txt"
with open(file_path, 'w') as file:
    file.write(passd)
    

print(file_path)

