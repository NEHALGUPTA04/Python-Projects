user_value = str(input("Enter the Phrase : "))
user_Phrase = user_value.split()
acronym = " "
for i in user_Phrase:
    acronym = acronym + str(i[0]).upper()

print(acronym)

