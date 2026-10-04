key = 0xaf

arr = bytearray(42)
arr[0:8]   = (0xe9fbecfbfae0fbfc).to_bytes(8, "little")
arr[8:16]  = (0xd9c2e6d89df5d8d4).to_bytes(8, "little")
arr[16:24] = (0xd6ceddedeadcdae1).to_bytes(8, "little")
arr[24:32] = (0xdce4e99c9deedfeb).to_bytes(8, "little")
arr[26:34] = (0xf8c0dce4e99c9dee).to_bytes(8, "little")
arr[34:42] = (0xd2c8ccf5e8ebddfb).to_bytes(8, "little")

flag = bytes(b ^ key for b in arr)
print(flag.decode())
