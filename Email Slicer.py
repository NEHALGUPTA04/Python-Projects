email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
slicing = (f"Your user name is '{username}' and your domain is '{domain}'")
print(slicing)
