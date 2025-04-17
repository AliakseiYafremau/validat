import validat

try:
   correct_email = "username@example.com"
   is_valid = validat.validate_email(correct_email)
except validat.EmailValidationError as e:
   print(f"Email validation error: {e.message}")

try:
   wrong_email = "username@@example.com"
   is_valid = validat.validate_email(wrong_email)
except validat.EmailValidationError as e:
   print(f"Email validation error: {e.message}")