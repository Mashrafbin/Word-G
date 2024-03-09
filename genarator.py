from tqdm import tqdm
import itertools
import time
import threading

# Characters 
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?'

yellow = "\033[93m"
white = "\033[0m"

print(yellow + '''
 ▄█     █▄   ▄██████▄     ▄████████ ████████▄          ▄██████▄  
███     ███ ███    ███   ███    ███ ███   ▀███        ███    ███ 
███     ███ ███    ███   ███    ███ ███    ███        ███    █▀  
███     ███ ███    ███  ▄███▄▄▄▄██▀ ███    ███       ▄███        
███     ███ ███    ███ ▀▀███▀▀▀▀▀   ███    ███      ▀▀███ ████▄  
███     ███ ███    ███ ▀███████████ ███    ███        ███    ███ 
███ ▄█▄ ███ ███    ███   ███    ███ ███   ▄███        ███    ███ 
 ▀███▀███▀   ▀██████▀    ███    ███ ████████▀         ████████▀  
                         ███    ███                              
            ---The ultimate wordlist genarator---
''')
print(white)

# Inputs
word_length = int(input("Word's length = "))
header = input("Header if you want, else press 'Enter': ")
extension = input("Extension if you want, else press 'Enter': ")
filename = input("File name: ") + ".txt"

# Function to generate passwords
def generate_passwords(file, pbar):
    for combination in itertools.product(characters, repeat=word_length):
        word = ''.join(combination)
        file.write(header + word + extension + '\n')
        pbar.update(1)  # Increment progress bar by 1 for each password generated

# Creating a file to save the combinations
with open(filename, 'w') as file:
    # Initialize tqdm progress bar
    pbar = tqdm(total=len(characters) ** word_length, desc="Generating passwords", unit=" words", colour= 'yellow')

    # Start generating passwords in a separate thread
    password_thread = threading.Thread(target=generate_passwords, args=(file, pbar))
    password_thread.start()

    # Wait for the password generation thread to finish
    password_thread.join()

    # Close tqdm progress bar
    pbar.close()

print("\nAll passwords have been saved to", filename)

print("Total number of combinations:", len(characters) ** word_length,"\neach words length= ",word_length,' digits')

time.sleep(4)
print(yellow + "quiting...")


