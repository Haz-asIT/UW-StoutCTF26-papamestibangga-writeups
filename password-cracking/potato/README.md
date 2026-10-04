# Potato

**Category:** Password Cracking  
**Points:** 35

Given hash:

```text
15bb45f9689592deb564fe48713565bf
```

The hint points to a legacy boot loader and a default credential.

Save the hash:

```bash
echo "15bb45f9689592deb564fe48713565bf" > potato_hash.txt
```

Use SecLists' default credential wordlist:

```bash
sudo apt update
sudo apt install seclists -y

john --format=Raw-MD5   --wordlist=/usr/share/seclists/Passwords/Default-Credentials/default-passwords.txt   potato_hash.txt

john --show --format=Raw-MD5 potato_hash.txt
```

Recovered password:

```text
tatercounter2000
```

Verify:

```bash
echo -n "tatercounter2000" | md5sum
```

Output:

```text
15bb45f9689592deb564fe48713565bf
```

If the platform expects the wrapper:

```text
STOUTCTF{tatercounter2000}
```
