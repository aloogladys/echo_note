# create a Person class with 4 attributes >> first_name, last_name, email, place_of_work
# create 3 instances of Person and print their first_name and last_name
# create a method that prints an email invite containg the last_name and place_of_work in the email
# add the 3 instances of person to a list, loop through the list and print their emails

# create one instance of person and set the first_name, last_name, email and place of work from user input



class Person ():
    def __init__(self,first_name, last_name, email, place_of_work ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.place_of_work = place_of_work

    def invite_email(self):
        print('hello ', self.first_name, self.last_name, 'welcome to our services')

        
personA = Person('gladys', 'aloo', 'aloogladys@gmail.com', 'roadstar')
personB = Person('hosea', 'mungai', 'mungaihoseaWgmail.com', 'Churpy')
personC = Person('Albert', 'Odongo', 'albertodongo@gmail.com', 'Navy')

first_name = input('first_name? ')
last_name = input ('last_name? ')
email = input('email? ')
place_of_work = input('place of work? ')

personD = Person (first_name, last_name, email, place_of_work)

person_list = (personA, personB, personC, personD)
for person in person_list:
    person.invite_email()

for person in person_list:
    print(person.email)





