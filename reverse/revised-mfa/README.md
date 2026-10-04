# Revised Multi-Factor Authentication

**Category:** Reverse Engineering  
**Points:** 40  
**File:** `main`

The challenge says:

> Okay, the MFA should have been fixed this time...

## 1. Check the binary

```bash
file ./main
```

The file is a stripped 64-bit Linux ELF.

## 2. Run it

```bash
chmod +x ./main
./main
```

Prompt:

```text
Enter value:
```

## 3. Locate the checker

```bash
strings -tx ./main
objdump -d -Mintel ./main
```

The program reads a value and passes it to a checking routine:

```asm
call printf
call scanf
mov  eax,DWORD PTR [rbp-0xc]
mov  edi,eax
call 13af
```

## 4. Recover the conditions

The preserved analysis identifies:

```text
input > 1000
input % 7 == 0
input % 191 == 0
input == 0x539
```

Convert the last constant:

```bash
python3 -c "print(0x539)"
```

Result:

```text
1337
```

And:

```text
1337 = 7 * 191
```

## 5. Get the flag

```bash
echo 1337 | ./main
```

Output:

```text
Enter value: STOUTCTF{bJgmJ8ID106VVesrL38BXR34PXOdBOB0}
```

## Flag

```text
STOUTCTF{bJgmJ8ID106VVesrL38BXR34PXOdBOB0}
```
