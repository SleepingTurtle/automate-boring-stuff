#! python 3
# Shitty password locker

PASSWORDS = {'email': 'shittypassword1',
             'blog': 'shittypasswords12',
             'porn acct': 'fishyvagina'}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + "copied to clipboard.")
else:
    print("There is no account name " + account)
