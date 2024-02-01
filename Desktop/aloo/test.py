# create a User class with attributes > username, email and password
# create a method called "validate_password" that takes in a string and checks if that string is equal
#       to the user's password the method will return True if the passwords match and false if they don't
# create three instances of the aformentioned class and save to a list
# create a login system using the information above.


class User():
    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password
    
    def validate_password(self, input_username, input_password):
        if self.password == input_password and self.username == input_username:
            return True
        else:
            return False




usera = User('aloo', 'aloo@gmail.com', 'password')
userb = User('hosea', 'hosea@gmail.com', 'hosea')
userc = User('nikita', 'nikita@gmail.com', 'nikita')

user_list = [usera, userb, userc]

username = input('enter username ')
password = input ('enter password ')


logged_in = False
 
for user in user_list:
    if user.validate_password (username, password) == True:
        logged_in = True
        break

if logged_in == False:
    print('wrong credentials, try again')
else:
    print ('You are logged in')



