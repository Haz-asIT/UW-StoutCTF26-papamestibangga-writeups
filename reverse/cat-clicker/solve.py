import base64

enc = "EDU7FjgqNy0eRDsKNgNeVSIHOwU7ISQyHBQ/UT5OY1YTNEMuDVhWACAP"
key = b"CatClickerMeow42"

raw = base64.b64decode(enc)
flag = bytes(raw[i] ^ key[i % len(key)] for i in range(len(raw))).decode()

print(flag)
