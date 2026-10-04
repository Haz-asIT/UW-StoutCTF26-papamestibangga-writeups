# Ghost Functions

**Category:** Reverse Engineering  
**Points:** 50  
**File:** `main`

Running the binary only prints:

```text
Theres something missing here.......
```

The write-up identified a second function that is not called by the normal execution path.

Inside that function:

```asm
mov BYTE PTR [rbp-0x49],0xaf
```

stores the XOR key. The function then loads encrypted bytes and later performs:

```asm
xor al,BYTE PTR [rbp-0x49]
```

before calling `puts`.

So the hidden routine:

1. stores encrypted flag bytes;
2. XORs each byte with `0xaf`;
3. prints the decoded flag.

Run the included reconstruction:

```bash
python3 solve.py
```

## Flag

```text
STOUTCTF{wZ2wImvNusEBrayDpA23FKsoWTrDGZcg}
```
