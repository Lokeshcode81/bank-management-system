
import streamlit as st
from hello import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered",
)

# Demo data is isolated to the current Streamlit session.
if "bank_data" not in st.session_state:
    st.session_state.bank_data = []

bank = Bank(st.session_state.bank_data)

st.title("🏦 Bank Management System")
st.caption("Portfolio Demo | Session-based temporary data")
st.warning(
    "Educational demo only. Do not enter real banking details "
    "or reuse a personal PIN. Data is temporary."
)

action = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Update Info",
        "Delete Account",
    ],
)

def account_credentials():
    account_number = st.text_input("Account Number")
    pin = st.text_input("4-digit PIN", type="password")
    return account_number.strip(), pin.strip()


if action == "Create Account":
    st.subheader("Create a New Account")

    with st.form("create_account_form"):
        name = st.text_input("Full Name")
        age = st.number_input(
            "Age", min_value=1, max_value=120, value=18, step=1
        )
        email = st.text_input("Email")
        pin = st.text_input("Create 4-digit PIN", type="password")
        confirm = st.form_submit_button("Create Account")

    if confirm:
        success, message, account_number = bank.create_account(
            name, int(age), email, pin
        )

        if success:
            st.success(message)
            st.info(f"Your demo account number: {account_number}")
            st.write("Save this account number for your current session.")
        else:
            st.error(message)


elif action == "Deposit":
    st.subheader("Deposit Money")

    with st.form("deposit_form"):
        account_number, pin = account_credentials()
        amount = st.number_input(
            "Deposit Amount",
            min_value=1,
            max_value=10000,
            value=100,
            step=1,
        )
        submit = st.form_submit_button("Deposit")

    if submit:
        success, message = bank.deposit(
            account_number, pin, int(amount)
        )
        (st.success if success else st.error)(message)


elif action == "Withdraw":
    st.subheader("Withdraw Money")

    with st.form("withdraw_form"):
        account_number, pin = account_credentials()
        amount = st.number_input(
            "Withdrawal Amount",
            min_value=1,
            value=100,
            step=1,
        )
        submit = st.form_submit_button("Withdraw")

    if submit:
        success, message = bank.withdraw(
            account_number, pin, int(amount)
        )
        (st.success if success else st.error)(message)


elif action == "Show Details":
    st.subheader("Account Details")

    with st.form("details_form"):
        account_number, pin = account_credentials()
        submit = st.form_submit_button("Show Details")

    if submit:
        user = bank.find_user(account_number, pin)

        if user:
            # Never display the PIN in account details.
            safe_details = {
                "Name": user["name"],
                "Age": user["age"],
                "Email": user["email"],
                "Account Number": user["account_number"],
                "Balance": user["balance"],
            }
            st.json(safe_details)
        else:
            st.error("Invalid account number or PIN.")


elif action == "Update Info":
    st.subheader("Update Account Information")
    st.caption("Leave a field blank if you do not want to change it.")

    with st.form("update_form"):
        account_number, pin = account_credentials()
        name = st.text_input("New Name (optional)")
        email = st.text_input("New Email (optional)")
        new_pin = st.text_input(
            "New 4-digit PIN (optional)", type="password"
        )
        submit = st.form_submit_button("Update Information")

    if submit:
        success, message = bank.update_user(
            account_number, pin, name, email, new_pin
        )
        (st.success if success else st.error)(message)


elif action == "Delete Account":
    st.subheader("Delete Demo Account")
    st.warning("This action cannot be undone within this session.")

    with st.form("delete_form"):
        account_number, pin = account_credentials()
        confirm_delete = st.checkbox("Yes, delete this demo account")
        submit = st.form_submit_button("Delete Account")

    if submit:
        if not confirm_delete:
            st.error("Please confirm account deletion.")
        else:
            success, message = bank.delete_user(
                account_number, pin
            )
            (st.success if success else st.error)(message)


st.divider()
st.caption(
    f"Demo accounts in this session: {len(st.session_state.bank_data)}"
)
