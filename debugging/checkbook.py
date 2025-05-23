class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance tracking.
    """

    def __init__(self):
        """
        Initializes a new Checkbook with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Args:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if funds are available.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop to interact with the user and perform deposit, withdrawal, or balance check.
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()
        if action == "exit":
            break
        elif action in ["deposit", "withdraw"]:
            try:
                amount = float(input("Enter the amount to {}: $".format(action)))
                if amount < 0:
                    print("Amount must be a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if action == "deposit":
                cb.deposit(amount)
            elif action == "withdraw":
                cb.withdraw(amount)
        elif action == "balance":
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
