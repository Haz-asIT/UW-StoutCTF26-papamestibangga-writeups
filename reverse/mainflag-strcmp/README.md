# mainflag / `strcmp`

> The official challenge title was not preserved in the source document. This entry uses the binary name `mainflag`.

The program asks for a flag and compares it using `strcmp`. A breakpoint on `strcmp` exposes the comparison string.

```bash
gdb -q ./mainflag
```

Inside GDB:

```gdb
break strcmp
run
```

Enter any test input:

```text
AAAA
```

When the breakpoint hits:

```gdb
x/s $rsi
```

The expected string is displayed:

```text
STOUTCTF{Hi2GZtWhAXAoEsotOtDoF94wN04Lm20Z}
```

## Flag

```text
STOUTCTF{Hi2GZtWhAXAoEsotOtDoF94wN04Lm20Z}
```
