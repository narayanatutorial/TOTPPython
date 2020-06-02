import pyotp
totp_uri=pyotp.totp.TOTP('KZ3UCY3GJNQWKWLDGFBW4RCLMJCUEZDJN5TGOZZWIVDDESTSG5FA').provisioning_uri("demo", issuer_name="Example")

print(totp_uri)