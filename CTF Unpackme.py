picoCTF 2022 — unpackme.py

Category  : Reverse Engineering
Difficulty: Medium
Tags      : packing, python
Flag      : picoCTF{175_chr157m45_5274ff21}

----------------------------------------------------------------

Objective

Reverse engineer a Python script that decrypts and executes a
hidden payload to recover the flag.

Tools Used

- Terminal (Kali Linux)
- Python 3
- nano (text editor)
- wget

----------------------------------------------------------------

Step 1: Downloading and Reading the Script

We start by downloading the provided Python file and reading
its contents.

    wget https://artifacts.picoctf.net/c/48/unpackme.flag.py
    cat unpackme.flag.py

The script reveals the following structure:

    import base64
    from cryptography.fernet import Fernet

    payload = b'gAAAAABkzWGO_8MlYpNM0n0o718LL...'

    key_str = 'correctstaplecorrectstaplecorrec'
    key_base64 = base64.b64encode(key_str.encode())
    f = Fernet(key_base64)
    plain = f.decrypt(payload)
    exec(plain.decode())

This tells us three things:

1. There is an encrypted payload inside the script.
2. The decryption key is already hardcoded in plain sight.
3. The decrypted result is passed directly to exec(), which
   runs it as Python code without showing us what it contains.

----------------------------------------------------------------

Step 2: Understanding the Danger of exec()

The exec() function executes whatever string is passed to it
as Python code. In this case, it blindly runs the decrypted
payload without revealing its contents to us.

This is a common obfuscation technique — the real logic of
the program is hidden inside an encrypted blob, and exec()
is used to run it silently at runtime.

To safely inspect what the payload contains, we simply need
to swap exec() for print().

----------------------------------------------------------------

Step 3: Modifying the Script

We open the file in nano and change the last line.

    nano unpackme.flag.py

Change:

    exec(plain.decode())

To:

    print(plain.decode())

Save and exit with Ctrl+X, then Y, then Enter.

----------------------------------------------------------------

Step 4: Running the Modified Script

    python3 unpackme.flag.py

The decrypted payload is now printed to the terminal instead
of being executed. It reveals the hidden Python program:

    pw = input('What\'s the password? ')

    if pw == 'batteryhorse':
        print('picoCTF{175_chr157m45_5274ff21}')
    else:
        print('That password is incorrect.')

The hidden program was a password checker. The correct
password is 'batteryhorse', and the flag is printed when
it is entered. Since we bypassed exec() entirely, we never
even needed to type the password.

----------------------------------------------------------------

Key Takeaway

The script used Fernet encryption (AES under the hood) to
hide its real logic. The decryption key was left hardcoded
in plain sight, and exec() was used to run the decrypted
code silently.

By replacing exec() with print(), we exposed the hidden
program without executing anything unknown — a safe and
effective reverse engineering technique.

----------------------------------------------------------------

Flag

picoCTF{175_chr157m45_5274ff21}

----------------------------------------------------------------
