pw=input("enter your password:")
pw1=input("enter your password again:")
if 8<=len(pw)<=12 and pw==pw1:
    print("password set")
else:
    print("error!!!")