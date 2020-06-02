import pyotp

base32secret = 'KZ3UCY3GJNQWKWLDGFBW4RCLMJCUEZDJN5TGOZZWIVDDESTSG5FA'
print('Secret:', base32secret)

totp = pyotp.TOTP(base32secret)
your_code = totp.now()
print(your_code);
print(totp.verify(your_code))