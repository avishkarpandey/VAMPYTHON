def create_file(filename, name, email):
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\nEmail: {email}\n")

def check_email(filename, email_to_check):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("Email:"):
                _, email = line.split(":", 1)
                if email.strip() == email_to_check:
                    return True
    return False

# Usage
filename = "user_info.txt"
create_file(filename, "John Doe", "john.doe@example.com")

# Get email input from user to check
email_input = input("Enter the email to check: ")

if check_email(filename, email_input):
    print("Email exists in the file.")
else:
    print("Email does not exist in the file.")
