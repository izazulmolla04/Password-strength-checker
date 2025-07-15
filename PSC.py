import re

def password_strenth_cheacker(password):
    if len(password) < 8:
        return "The password is weak because it is less than 8 characters long."
    
    if not re.search(r"[A-Z]", password):
        return "The password is weak that you have entered because it does not contain an uppercase letter."
    
    if not re.search(r"[a-z]", password):
        return "The password is weak that you have entered because it does not contain a lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "The password is weak that you have entered because it does not contain a digit."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "The password is weak that you have entered because it does not contain a special character."
    
    return "The password is strong that you have entered."

def main():
    while True:
        password=input("Enter a password to check its strength (or type 'exit' to quit): ")

        if password.lower()=="exit":
            print(" Thank you for using the password strength checker. Goodbye!")
            break

        result = password_strenth_cheacker(password)
        print(result)

if __name__ == "__main__":
    main()