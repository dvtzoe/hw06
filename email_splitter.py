email = input("Email: ")

at_sign_position = email.find("@")

username = email[:at_sign_position]
domain = email[at_sign_position + 1 :]

if at_sign_position != -1 and username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email")
