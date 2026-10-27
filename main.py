import pandas as pd
from collections import deque

# Keep employees_50.xlsx in the same folder as this file.
employees = pd.read_excel("employees_50.xlsx")

accounts = {}

# ---------------- TRANSACTION LINKED LIST ----------------
class TransactionNode:
    def __init__(self, acc_no, transaction, amount):
        self.acc_no = acc_no
        self.transaction = transaction
        self.amount = amount
        self.next = None


class TransactionList:
    def __init__(self):
        self.head = None

    def add(self, acc_no, transaction, amount):
        node = TransactionNode(acc_no, transaction, amount)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def show(self):
        print("\n===== TRANSACTION LINKED LIST =====")
        current = self.head
        if current is None:
            print("No transactions found.")
            return
        while current is not None:
            print(f"{current.acc_no} - {current.transaction} - Rs. {current.amount}")
            current = current.next


transaction_list = TransactionList()

# ---------------- TRANSACTION STACK ----------------
class TransactionStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def show(self):
        print("\n===== TRANSACTION STACK (LATEST FIRST) =====")
        if not self.items:
            print("No transactions found.")
            return
        for item in reversed(self.items):
            print(item)


transaction_stack = TransactionStack()

# ---------------- CUSTOMER QUEUE ----------------
class CustomerQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, name):
        self.queue.append(name)
        print("Customer added to queue.")

    def serve_customer(self):
        if not self.queue:
            print("Queue is empty.")
            return
        print("Customer served:", self.queue.popleft())

    def show_queue(self):
        print("\n===== CUSTOMER QUEUE =====")
        if not self.queue:
            print("Queue is empty.")
            return
        for i, name in enumerate(self.queue, start=1):
            print(f"{i} - {name}")


customer_queue = CustomerQueue()

total_deposit = 0.0
total_withdraw = 0.0
deposit_count = 0
withdraw_count = 0


# ---------------- BANK ACCOUNT CLASSES ----------------
class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.history = ["Account created"]

    def deposit(self, amount):
        global total_deposit, deposit_count
        if amount <= 0:
            print("Invalid amount. Enter a positive amount.")
            return
        self.balance += amount
        total_deposit += amount
        deposit_count += 1
        self.history.append(f"Deposited Rs.{amount}")
        transaction_list.add(self.acc_no, "Deposit", amount)
        transaction_stack.push(f"{self.acc_no} - Deposit - Rs. {amount}")
        print("Deposit successful.")

    def withdraw(self, amount):
        global total_withdraw, withdraw_count
        if amount <= 0:
            print("Invalid amount. Enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            total_withdraw += amount
            withdraw_count += 1
            self.history.append(f"Withdrawn Rs.{amount}")
            transaction_list.add(self.acc_no, "Withdrawal", amount)
            transaction_stack.push(f"{self.acc_no} - Withdrawal - Rs. {amount}")
            print("Withdrawal successful.")


class SavingsAccount(Account):
    def show(self):
        print("\nAccount Number:", self.acc_no)
        print("Name:", self.name)
        print("Balance: Rs.", self.balance)


def create_account():
    acc_no = input("Enter account number: ").strip()
    if not acc_no:
        print("Account number cannot be empty.")
        return
    if acc_no in accounts:
        print("Account already exists.")
        return
    name = input("Enter name: ").strip()
    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if balance < 0:
        print("Invalid balance.")
        return
    accounts[acc_no] = SavingsAccount(acc_no, name, balance)
    print("Account created successfully.")


def deposit():
    acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    accounts[acc_no].deposit(amount)


def withdraw():
    acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    accounts[acc_no].withdraw(amount)


def show_account():
    acc_no = input("Enter account number: ").strip()
    if acc_no not in accounts:
        print("Account not found.")
        return
    account = accounts[acc_no]
    account.show()
    print("\nTransaction History:")
    for item in account.history:
        print("-", item)


def daily_report():
    print("\n===== DAILY TRANSACTION REPORT =====")
    print("Total Deposits: Rs.", total_deposit)
    print("Total Withdrawals: Rs.", total_withdraw)
    print("Number of Deposits:", deposit_count)
    print("Number of Withdrawals:", withdraw_count)
    print("Net Transaction: Rs.", total_deposit - total_withdraw)


# ---------------- EMPLOYEE DATA / SEARCH / SORT ----------------
def employee_data():
    print("\n===== EMPLOYEE DATA =====")
    print("Total Employees:", len(employees))
    print("\nFirst 5 Employees:")
    for _, row in employees.head(5).iterrows():
        print(row.to_dict())


def search_employee():
    emp_id = input("Enter Employee ID to search: ").strip().lower()
    matches = employees[employees["Employee_ID"].astype(str).str.lower() == emp_id]
    if matches.empty:
        print("Employee not found.")
        return
    row = matches.iloc[0]
    print("\n===== EMPLOYEE FOUND =====")
    for column in ["Employee_ID", "Employee_Name", "Department", "Role",
                   "Salary", "Experience_Years", "Age", "Branch"]:
        if column in employees.columns:
            print(f"{column.replace('_', ' ')}: {row[column]}")


def sort_salary():
    data = employees.to_dict("records")
    # Bubble sort: descending salary order.
    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if data[j]["Salary"] < data[j + 1]["Salary"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print("\n===== EMPLOYEES SORTED BY SALARY =====")
    for row in data[:5]:
        print(row["Employee_ID"], "-", row["Employee_Name"], "- Rs.", row["Salary"])


# ---------------- SALARY BINARY SEARCH TREE ----------------
class SalaryNode:
    def __init__(self, salary, emp_id, name):
        self.salary = salary
        self.emp_id = emp_id
        self.name = name
        self.left = None
        self.right = None


class SalaryBST:
    def __init__(self):
        self.root = None

    def insert(self, salary, emp_id, name):
        node = SalaryNode(salary, emp_id, name)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if salary < current.salary:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.emp_id} - {node.name} - Rs. {node.salary}")
            self.inorder(node.right)

    def show(self):
        print("\n===== EMPLOYEES USING BINARY SEARCH TREE =====")
        if self.root is None:
            print("BST is empty.")
            return
        self.inorder(self.root)


salary_bst = SalaryBST()


def build_salary_bst():
    salary_bst.root = None
    for _, row in employees.iterrows():
        salary_bst.insert(
            int(row["Salary"]),
            str(row["Employee_ID"]),
            str(row["Employee_Name"])
        )


def show_salary_bst():
    build_salary_bst()
    salary_bst.show()


def search_salary_bst():
    build_salary_bst()
    try:
        salary = int(input("Enter salary to search: "))
    except ValueError:
        print("Please enter a valid salary.")
        return
    current = salary_bst.root
    while current is not None:
        if salary == current.salary:
            print("\nEmployee Found in BST")
            print("Employee ID:", current.emp_id)
            print("Name:", current.name)
            print("Salary:", current.salary)
            return
        if salary < current.salary:
            current = current.left
        else:
            current = current.right
    print("Employee with this salary not found.")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n===== BANKING MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. Daily Transaction Report")
        print("6. Employee Data")
        print("7. Exit")
        print("8. Search Employee")
        print("9. Sort Employees by Salary")
        print("10. Show Transaction Linked List")
        print("11. Show Transaction Stack")
        print("12. Add Customer")
        print("13. Serve Customer")
        print("14. Show Customer Queue")
        print("15. Show Employees Using BST")
        print("16. Search Employee by Salary using BST")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_account()
        elif choice == "5":
            daily_report()
        elif choice == "6":
            employee_data()
        elif choice == "7":
            print("Thank you!")
            break
        elif choice == "8":
            search_employee()
        elif choice == "9":
            sort_salary()
        elif choice == "10":
            transaction_list.show()
        elif choice == "11":
            transaction_stack.show()
        elif choice == "12":
            name = input("Enter customer name: ").strip()
            if name:
                customer_queue.add_customer(name)
            else:
                print("Customer name cannot be empty.")
        elif choice == "13":
            customer_queue.serve_customer()
        elif choice == "14":
            customer_queue.show_queue()
        elif choice == "15":
            show_salary_bst()
        elif choice == "16":
            search_salary_bst()
        else:
            print("Invalid choice. Select an option from 1 to 16.")


if __name__ == "__main__":
    main()
