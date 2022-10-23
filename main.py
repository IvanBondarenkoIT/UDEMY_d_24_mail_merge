#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def create_letter(name):
    with open(f'Input/Letters/starting_letter.txt', mode='r') as file:
    # with open("saves.txt", mode="w") as file:
        list_ = file.readlines()
        print(list_)
        list_[0] = list_[0].replace("[name],", f"{name},")
        print("".join(list_))

    with open(f'Output/ReadyToSend/{name}_letter.txt', mode='w') as new_file:
         new_file.write("".join(list_))



def get_guests():
    with open(f'Input/Names/invited_names.txt', mode='r') as file:
        text = file.readlines()
        #list_names = text.split()
        for name in text:
            # print(name.strip())
            create_letter(name.strip())


get_guests()


'''Aang
Zuko
Appa
Katara
Sokka
Momo
Uncle Iroh
Toph'''