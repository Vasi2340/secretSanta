import smtplib, ssl, getpass,random
# from rich import print
from sys import stdin, exit

# scanning names
names = []
print("Enter the names of the participants: ")
print("(press enter after every name and ctrl+D ends input)")
for line in stdin:
    if line == '': 
        break

    names.append(line.strip())
    


# n is the number of people participating
n = len(names)


# scanning emails
i = 0
emails = []
while i < n:
    print("Enter email of " + names[i])
    line = stdin.readline()
    emails.append(line.strip())
    i = i+1


# printing the inputed names and emails for easy check
i = 0
while i < n:
    print(names[i] + ": " + emails[i] )
    i = i+1
print('')

print("Enter cost limit: ")
limit = stdin.readline().strip()

# requirements for list being ok
def listOk(list2):
    n = len(list2)
    if n < 2:
        print("Run again and enter more than 2 participants next time.")
        exit()
    i = 0
    # against selfgifting
    while i < n:
        if list2[i] == i:
            return False
        i = i+1
    
    return True

# shuffling the participants
def santaShuffle(n):
    list1 = list(range(0,n))
    list2 = list(range(0,n))
    random.shuffle(list2)
    

    while 1:
        if listOk(list2):
            break
        random.shuffle(list2)
    
    finalList = []
    i = 0
    while i < n:
        finalList.append([i,list2[i]])
        i = i+1
    
    return finalList

shuffledList = santaShuffle(n)


print("\nThe participants have been shuffled!")


# smtp mail stuff
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
print("\nEnter the sender email adress: ")
print('\033[93m' + "NOTE: The email should be a gmail account with allowed access to less secure programs." + '\033[0m')
print('\033[92m' + "More info here: [https://www.lifewire.com/allow-email-programs-access-to-gmail-with-password-1171875]" + '\033[0m')
sender_email  = stdin.readline().strip()  # Enter your address
print("\nEnter password")
password = getpass.getpass("Type your password and press enter: ")

message = """\
Subject: SecretSanta Ho Ho Ho

In this email is the name of the person for whom you are buying a gift. Don't tell anyone!
\n\nThe person for whom you are buying a gift is: 
"""

message1 = "\n\nThe gift cost shouldn't be more than " + limit + " bucks.\n\n"
print("\nAdditional message (like party date and place): ")
print("(ctrl+D ends input)")
message1 = message1 + stdin.read()

print('\033[96m' + "\nSending..." + '\033[0m')
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        i = 0
        while i < n:
            receiver_email = emails[i]
            
            server.sendmail(sender_email, receiver_email, message + names[shuffledList[i][1]] + message1)
            i = i+1

print('\033[94m' + "Messages sent successfully!" + '\033[0m')