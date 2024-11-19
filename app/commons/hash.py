import hashlib 

def hash(str):
  return hashlib.sha512(str.encode()).hexdigest()