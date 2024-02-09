import bcrypt

login = "HelloTom"

hashLogin = bcrypt.hashpw(login.encode("utf-8"), bcrypt.gensalt())
print(hashLogin.decode("utf-8"))
print(bcrypt.checkpw(login.encode("utf-8"),hashLogin))