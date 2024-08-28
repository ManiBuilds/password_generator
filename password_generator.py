import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True):
    
    letters = string.ascii_letters
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''
    
    
    all_characters = letters + digits + symbols
    
    password = []
    if include_digits:
        password.append(random.choice(digits))
    if include_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(letters))
    
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired length of the password (default 12): ") or 12)
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, include_digits, include_symbols)
    
    print("\nGenerated Password: ", password)

if __name__ == "__main__":
    main()
