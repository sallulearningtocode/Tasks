from pwdgenlib import PasswordGenerator

# Create a PasswordGenerator instance
password_generator = PasswordGenerator()

# Generate a random password
password = password_generator.generate_password()

# Get the generated password
print(password)
