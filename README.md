# pysafe
Yet Another Homemade Credential Store

## Warning

This is an experimental code : do not use in production neither for (highly) sensitive credentials.
For example, it does not implement a secure delete solution to remove your passwords from RAM.

## Dependencies

- pyperclip
- simplecrypt

## Usages

Initiates a new safe (in safe.enc) with the following command:
```bash
$ ./pysafe.py create safe.enc "My Safe"
```

Stores a new password in safe.enc
```bash
$ ./pysafe.py store my_cred_name --keypass safe.enc 
```

List all creadentials stored in safe.enc
```bash
$ ./pysafe.py list --keypass safe.enc
```

Retrieves credentials attached to "my_cred_name"  stored in safe.enc and stores it in your clipboard
```bash
$ ./pysafe.py get my_cred_name --keypass safe.enc

```

Retrieves credentials attached to "my_cred_name" stored in safe.enc and displays it
```bash
$ ./pysafe.py get my_cred_name --keypass safe.enc

```

Deletes one credential info from safe.enc
```bash
$ ./pysafe.py delete my_cred_name --keypass safe.enc
```
