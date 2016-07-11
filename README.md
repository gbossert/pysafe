# pysafe
Yet Another Homemade Credential Store

## Warning

This is an experimental code : do not use in production neither for (highly) sensitive credentials.
For example, it does not implement a secure delete solution to remove your passwords from RAM.

## Crypto ?

Your credentials are stored in an encrypted file. Encryption relies on the python simplecrypt library (https://github.com/andrewcooke/simple-crypt).
As detailed in their documentation, the following cryptographic rules are followed:

* The password is expanded to two 256 bit keys using PBKDF2 with a 256 bit random salt (increased from 128 bits in release 3.0.0), SHA256, and 100,000 iterations (increased from 10,000 in release 4.0.0).
* AES256 CTR mode is used to encrypt the data with one key. The first 64 bits of the salt are used as a message nonce (of half the block size); the incremental part of the counter uses the remaining 64 bits (see section B.2 of http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf).
* An encrypted messages starts with a 4 byte header ("sc" in ASCII followed by two bytes containing version data).
* An SHA256 HMAC (of header, salt, and encrypted message) is calculated using the other key.
* The final message consists of the header, salt, encrypted data, and HMAC, concatenated in that order.
* On decryption, the header is checked and the HMAC validated before decryption.


## Dependencies

- pyperclip
- simple-crypt

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
$ ./pysafe.py get my_cred_name --keypass safe.enc --show-password

```

Deletes one credential info from safe.enc
```bash
$ ./pysafe.py delete my_cred_name --keypass safe.enc
```
