import random as ran
import array

def passprompt():
    while True:
        c = input("Do You Want to Generate a Password(Y/N)? ")
        if c=='Y' or c=="y": ch = True
        if c=='N' or c=='n': ch = False
        break
    return ch


def password_gen():
    # maximum length of password needed
    while True:
        try:
            pass_len = int(input("Enter The Password Length: "))
        except:
            print("Please Enter A Numeric Value.")
            continue
        break

    #Array of every possible character seperated by their types and all available under dictionary
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z']
     
    upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
              'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
              'Z']
     
    symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
              '*', '(', ')', '<']

     
    # combines all the character arrays above to form one array
    jumbled_mess = num + upcase + lowcase + symbol
     
    # randomly select at least one character from each character set above
    rand_digit = ran.choice(num)
    rand_upper = ran.choice(upcase)
    rand_lower = ran.choice(lowcase)
    rand_symbol = ran.choice(symbol)
     
    # combine the character ranly selected above at this stage, the password contains only 4 characters but
    # we want a 12-character password
    infant_pass = rand_digit + rand_upper + rand_lower + rand_symbol
     
     
    # now that we are sure we have at least one character from each set of characters, we fill the rest of
    # the password length by selecting ranly from the combined list of character above.
    for x in range(pass_len - 4):
        infant_pass = infant_pass + ran.choice(jumbled_mess)
     
        # convert temporary password into array and shuffle to prevent it from having a consistent pattern
        # where the beginning of the password is predictable making it truly random
        infant_pass_list = array.array('u', infant_pass)
        ran.shuffle(infant_pass_list)
     
    # traverse the temporary password array and append the chars to form the password
    password = ""
    for x in infant_pass_list:
            password = password + x

    return password

#testing
#passprompt()
#password_gen()
