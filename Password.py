import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    character_pool = ''

    if use_letters:
        character_pool += string.ascii_letters  # A-Z, a-z
    if use_digits:
        character_pool += string.digits          # 0-9
    if use_symbols:
        character_pool += string.punctuation     # Special characters

    if not character_pool:
        print("Error: You must select at least one character type!")
        return None

    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("\n--- Random Password Generator ---\n")

    
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    
    password = generate_password(length, use_letters, use_digits, use_symbols)

    if password:
        print(f"\nYour Random Password: {password}\n")

if __name__ == "__main__":
    main()
