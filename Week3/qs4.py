BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
pw =input("Enter your password")
pw1 =input("enter your password again")
if 8=<len(pw)<=12 and pw==pw1:
    if pw not in BAD_PASSWORDS and pw1 not in BAD_PASSWORDS:
        print("password set")
    else:
        print("bad password")
else:
    print("error!!")