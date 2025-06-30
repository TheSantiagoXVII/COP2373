import re

# Function made for the validation of the phone numbers
def validate_phone_number(phone_number):
    pattern = re.compile(r'^(?:\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}$')
    return bool(pattern.match(phone_number))

# Function made for the validation of the social security numbers
def validate_ssn(ssn):
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# Function made to validate the digits introduced as the zip code.
def validate_zip_code(zip_code):
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

# Main function requiring the user to introduce the information + Validation
def main():
    # Get user input
    phone_number = input("Enter the phone number (XXX-XXX-XXXX or (XXX) XXX-XXXX): ")
    ssn = input("Enter the Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter the ZIP code (##### or #####-####): ")

    # Validate the inputs
    is_phone_valid = validate_phone_number(phone_number)
    is_ssn_valid = validate_ssn(ssn)
    is_zip_valid = validate_zip_code(zip_code)

    # Output results
    print("\nValidation Results:")
    print(f"Phone Number: {is_phone_valid}")
    print(f"SSN: {is_ssn_valid}")
    print(f"ZIP Code: {is_zip_valid}")

# Main function
if __name__ == "__main__":
    main()
