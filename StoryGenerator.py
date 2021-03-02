import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 26th Jan']
who = ['a Software Engineer', 'a Data Scientist', 'a SI', 'a SI','a IAS']
name = ['MUTTU', 'AAYU','JAYA', 'YAMI', 'RDANGI']
residence = ['MP','GJ', 'RJ', 'MH', 'UP']
went = ['Office', 'lab','seminar', 'college', 'coaching']
happened = ['made a lot of work','Data analysis', 'found a explosure','submitted work','wrote a book']
print(random.choice(when) + ', ' + random.choice(who) +  ' that lived in ' + random.choice(residence) +  " named "+random.choice(name) +', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
