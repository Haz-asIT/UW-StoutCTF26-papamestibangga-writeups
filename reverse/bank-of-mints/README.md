# Bank of Mints

**Category:** Reverse Engineering  
**Points:** 85  
**File:** `main`

The binary asks for a username and password.

`strings` reveals users `user0` through `user19`. The disassembly shows a fixed-size user database, with records of `0x98` bytes starting at address `0x20e0`.

The included `dump_users.py` parses:

- username from the first 100 bytes;
- password at offset 100;
- permission at offset 104.

Important output:

```text
10 user10 839666900 1
```

Credentials:

```text
Username:   user10
Password:   839666900
Permission: 1
```

Test them:

```bash
printf 'user10\n839666900\n' | ./mainbank
```

The terminal display shows:

```text
Flag: STOUTCTF{VvQQMy5AsYaYf1oN9xz6kQBqN:y5DHY}
```

## Non-printable byte note

The source write-up states that there is a non-printable byte `0x19` after the colon. Therefore the exact flag bytes are:

```python
b"STOUTCTF{VvQQMy5AsYaYf1oN9xz6kQBqN:\x19y5DHY}"
```

That byte is not visible in the normal terminal rendering.
