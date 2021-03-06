# Initializing our (empty) blockchain list
genesis_block = {"hash": "", "index": 0, "transactions": []}
blockchain = [genesis_block]
open_transactions = []
owner = "Jacob"


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: person who sent the coin
        :recipient: person receiving the coin
        :amount: the amount of coin in the transaction (default to 1.0)
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = []
    hashed_block = "-".join([str(last_block[key]) for key in last_block])
    print(hashed_block)

    # hashed_block = ""
    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)

    print(hashed_block)

    block = {
        "hash": "hashed_block",
        "index": len(blockchain),
        "transactions": open_transactions,
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction amount please: "))
    # this returns a tuple, but the () are not needed
    return tx_recipient, tx_amount


def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """ Output all blocks of the blockchain. """
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    pass


waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        mine_block()
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "h":
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        # This will lead to the loop to exist because it's running condition becomes False
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print("Invalid blockchain!")
    #     # Break out of the loop
    #     break
else:
    print("User left!")


print("Done!")
