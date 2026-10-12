
import random
import string


class Bank:
    def __init__(self, data):
        # The list belongs to the current Streamlit session.
        self.data = data

    def generate_account_number(self):
        while True:
            letters = "".join(
                random.choices(string.ascii_uppercase, k=3)
            )
            digits = "".join(random.choices(string.digits, k=3))
            special = random.choice("!@#$%")

            chars = list(letters + digits + special)
            random.shuffle(chars)
            account_number = "".join(chars)

            if not any(
                user["account_number"] == account_number
                for user in self.data
            ):
                return account_number

    def create_account(self, name, age, email, pin):
        name = name.strip()
        email = email.strip()
        pin = str(pin).strip()

        if not name or not email:
            return False, "Name and email are required.", None

        if age < 18:
            return False, "Account creation is only available for age 18+ in this demo.", None

        if not pin.isdigit() or len(pin) != 4:
            return False, "PIN must contain exactly 4 digits.", None

        account_number = self.generate_account_number()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_number": account_number,
            "balance": 0,
        }

        self.data.append(user)
        return True, "Account created successfully.", account_number

    def find_user(self, account_number, pin):
        account_number = str(account_number).strip()
        pin = str(pin).strip()

        for user in self.data:
            if (
                user["account_number"] == account_number
                and user["pin"] == pin
            ):
                return user

        return None

    def deposit(self, account_number, pin, amount):
        user = self.find_user(account_number, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        if amount < 1 or amount > 10000:
            return False, "Deposit amount must be between 1 and 10,000."

        user["balance"] += amount
        return True, f"Deposit successful. New balance: {user['balance']}"

    def withdraw(self, account_number, pin, amount):
        user = self.find_user(account_number, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        if amount < 1:
            return False, "Withdrawal amount must be greater than zero."

        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount
        return True, f"Withdrawal successful. New balance: {user['balance']}"

    def update_user(
        self, account_number, pin, name="", email="", new_pin=""
    ):
        user = self.find_user(account_number, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        if name.strip():
            user["name"] = name.strip()

        if email.strip():
            user["email"] = email.strip()

        if str(new_pin).strip():
            new_pin = str(new_pin).strip()

            if not new_pin.isdigit() or len(new_pin) != 4:
                return False, "New PIN must contain exactly 4 digits."

            user["pin"] = new_pin

        return True, "Account information updated successfully."

    def delete_user(self, account_number, pin):
        user = self.find_user(account_number, pin)

        if user is None:
            return False, "Invalid account number or PIN."

        self.data.remove(user)
        return True, "Demo account deleted successfully."
