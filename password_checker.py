import getpass
import string

print("=" * 35)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 35)
print("Your password is analyzed locally and is not stored.")

common_passwords = [
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "letmein",
    "admin",
    "welcome"
]

common_sequences = [
    "1234",
    "2345",
    "3456",
    "abcd",
    "bcde",
    "qwerty",
    "123456",
    "abcdef",
    "password",
    "qwerty123"
]

password = getpass.getpass("Enter your password:")
if not password:
    print("Password cannot be empty.")
    exit()
password_length = len(password)
score = 0
suggestions = []
normalized_password = password.lower()

print("\n--- Security Analysis ---\n")

# Length check
if password_length < 8:
    print("Length check: Failed")
    suggestions.append("Use at least 8 characters.")
elif password_length <= 10:
    score += 1
    print("Length check: Passed (1 point)")
elif password_length <= 14:
    score += 2
    print("Length check: Passed (2 points)")
else:
    score += 3
    print("Length check: Passed (3 points)")

# Lowercase check
lowercase_found = False    
for character in password:
    if character.islower():
        lowercase_found = True
        break 
if lowercase_found:
        score +=1
        print("Lowercase check: Passed")  
else:
        print("Lowercase check: Failed")
        suggestions.append("Add at least one lowercase letter.")
        
# Uppercase check        
uppercase_found = False        
for character in password:
    if character.isupper():
        uppercase_found = True
        break
if uppercase_found:
        score +=1
        print("Uppercase check: Passed")
else:
        print("Uppercase check: Failed")
        suggestions.append("Add at least one uppercase letter.")

# Number check        
number_found = False        
for character in password:
    if character.isdigit():
        number_found = True
        break
if number_found:
        score +=1
        print("Number check: Passed")
else:
        print("Number check: Failed")
        suggestions.append("Add at least one number.")

# Special character check        
special_found = False        
for character in password:
    if character in string.punctuation:
        special_found = True
        break
if special_found:
        score +=1
        print("Special character check: Passed")
else:
        print("Special character check: Failed")
        suggestions.append("Add at least one special character.")

# Common password check                
if normalized_password in common_passwords:
    print("Common password: Yes")
    suggestions.append("Avoid common or easily guessed passwords.")
else:
    score +=1
    print("Common password: No")

# Consecutive repetition check    
repetition_found = False
for i in range(2, len(password)):
    if password[i] == password[i-1] == password[i-2]:
        repetition_found = True
        break
if repetition_found:
    print("Consecutive repetition: Yes")    
    suggestions.append("Avoid repeating the same character three or more consecutive times.")
else:
    score +=1
    print("Consecutive repetition: No")

# Predicable sequence check        
sequence_found = False
for sequence in common_sequences:
    if sequence in normalized_password:
        sequence_found = True
        break
if sequence_found:
    print("Predictable sequence: Yes")    
    suggestions.append("Avoid using predictable sequences like '1234' or 'abcd'.")
else:
    score +=1
    print("Predictable sequence: No")

# Final score 
print("\n--- Final Score ---")   
print("\nScore:", score, "/10")    

#Strength rating
if score <= 3:
    print("Strength: Very Weak")
    print("Advice: Your password is very weak and should be changed.")
elif score <= 5:
    print("Strength: Weak")
    print("Advice: Your password has several weaknesses. Consider improving it.")
elif score <= 7:
    print("Strength: Moderate")
    print("Advice: Your password is okay, but it can be improved for better security.")
elif score <= 9:
    print("Strength: Strong")
    print("Advice: Your password is strong and meets most security criteria.")
else:
    print("Strength: Very Strong")
    print("Advice: Your password passed all current security checks.")

# Suggestions
print("\n--- Suggestions ---\n")
if suggestions:
    for suggestion in suggestions:
        print("-", suggestion)
else:
     print("No suggestions. Your password passed all checks!")            