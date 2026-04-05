CTF Writeup: Patchme.py
picoCTF | Reverse Engineering Challenge


-----------------------------------------------------------
WHAT WAS THIS CHALLENGE?
-----------------------------------------------------------

Two files were provided: patchme.flag.py and flag.txt.enc. The Python script when run correctly would decrypt the encrypted flag file and reveal the answer. The key was finding the correct password hidden inside the Python source code.


-----------------------------------------------------------
STEP 1 - Download Both Files
-----------------------------------------------------------

Commands used:
wget https://artifacts.picoctf.net/c/201/patchme.flag.py
wget https://artifacts.picoctf.net/c/201/flag.txt.enc

What happened:
Both files were downloaded into the current directory. ls confirmed they were both present. It is important both files are in the same directory because the Python script opens flag.txt.enc directly by filename.

Remember: when a challenge gives you multiple files, always download all of them and keep them in the same directory.


-----------------------------------------------------------
STEP 2 - Read the Python File
-----------------------------------------------------------

Command used: cat patchme.flag.py

What happened:
Reading the file revealed a function called level_1_pw_check. This function asks the user to enter a password and checks it against a hardcoded value split across multiple lines:

if( user_pw == "ak98" +
               "-=90" +
               "adfjhgj321" +
               "sleuth9000"):

The password was split into four pieces joined together with the + operator. Joining them gives the full password.

Remember: developers sometimes split strings across multiple lines for readability. Always join them together mentally when reading code.


-----------------------------------------------------------
STEP 3 - Reconstruct the Password
-----------------------------------------------------------

The four pieces joined together:
ak98 + -=90 + adfjhgj321 + sleuth9000

Full password: ak98-=90adfjhgj321sleuth9000

A common mistake here is missing the -= part of the second piece. Reading carefully matters.

Remember: join string pieces exactly as written. No spaces, no missing characters.


-----------------------------------------------------------
STEP 4 - Run the Script and Enter the Password
-----------------------------------------------------------

Command used: python3 patchme.flag.py

What happened:
The script asked for the vault password. Entering ak98-=90adfjhgj321sleuth9000 passed the check, the script decrypted flag.txt.enc using the password as the key, and printed the flag.

Remember: python3 filename.py runs a Python script. Always make sure you are in the same directory as any files the script depends on.


-----------------------------------------------------------
QUICK REFERENCE
-----------------------------------------------------------

wget URL                        Download a file from the internet
cat patchme.flag.py             Read and understand the source code
Join split strings              ak98 + -=90 + adfjhgj321 + sleuth9000
python3 patchme.flag.py         Run the script and enter the password


-----------------------------------------------------------
THE FLAG
-----------------------------------------------------------

Obtained after entering the correct password: ak98-=90adfjhgj321sleuth9000


-----------------------------------------------------------
KEY TAKEAWAYS
-----------------------------------------------------------

When multiple files are provided, read all of them before doing anything. The relationship between files is often the key to the solution.

Passwords hardcoded in source code are a real vulnerability. In CTFs this is intentional. In real software it is a serious security flaw.

String concatenation split across multiple lines is easy to misread. Always reconstruct the full string carefully and do not skip any piece.

The password check function is always worth finding. It is the gatekeeper and almost always contains or points to the answer.
