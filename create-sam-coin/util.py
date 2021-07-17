from algosdk import account, mnemonic

def generate_new_account():
    """
    Generate a new Algorand account and print the public address
    and private key mnemonic.
    """
    private_key, public_address = account.generate_account()
    passphrase = mnemonic.from_private_key(private_key)
    print("Address: {}\nPassphrase: \"{}\"".format(public_address, passphrase))

if __name__ == "__main__":
    generate_new_account()
    generate_new_account()