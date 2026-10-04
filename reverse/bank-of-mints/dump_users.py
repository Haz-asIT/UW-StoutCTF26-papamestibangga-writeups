import struct

data = open("./mainbank", "rb").read()

base = 0x20e0
record_size = 0x98

for i in range(20):
    record = data[base + i*record_size : base + (i+1)*record_size]
    username = record[:100].split(b"\x00")[0].decode()
    password = struct.unpack_from("<i", record, 100)[0]
    permission = struct.unpack_from("<i", record, 104)[0]
    print(i, username, password, permission)
