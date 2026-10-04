# President!

**Category:** Password Cracking  
**Points:** 35

Given hash:

```text
5af6de809f58e7eb0d698edc488b1376
```

The hint points to an old president's pet and says to replace spaces with underscores.

The source write-up identifies William Howard Taft's cow:

```text
Mooly Wooly
```

Candidate:

```text
Mooly_Wooly
```

Verify:

```bash
echo -n "Mooly_Wooly" | md5sum
```

Output:

```text
5af6de809f58e7eb0d698edc488b1376
```

Optional John check:

```bash
echo "Mooly_Wooly" > pets.txt
echo "5af6de809f58e7eb0d698edc488b1376" > president_hash.txt

john --format=Raw-MD5 --wordlist=pets.txt president_hash.txt
john --show --format=Raw-MD5 president_hash.txt
```

Recovered password:

```text
Mooly_Wooly
```

If the platform expects the competition wrapper:

```text
STOUTCTF{Mooly_Wooly}
```
