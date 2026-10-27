# Banking Management System Using Python and Data Structures

**Student:** Abhishek Kumar  
**Registration No.:** 251302219  
**Course:** B.Tech CSE AIML – 3D  
**University:** SGT University

## Project Overview

The Banking Management System is a menu-driven Python console application created as an academic Data Structures and Algorithms (DSA) project. It demonstrates basic banking operations and uses data structures to manage transaction records, customer service, and employee information.

## Features

- Create a bank account
- Deposit money and withdraw money
- Display account details and transaction history
- Generate a daily transaction report
- Read employee records from an Excel file
- Search for an employee by ID
- Sort employees by salary
- Display transaction records using a linked list
- Display transaction records using a stack
- Add customers to a queue, serve customers, and display the queue
- Display employee records using a Binary Search Tree (BST)
- Search for an employee by salary using the BST

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Pandas
- OpenPyXL
- Excel (`.xlsx`)
- Data structures: Linked List, Stack, Queue, and Binary Search Tree

## Project Files

```text
Banking_DSA_Project/
├── main.py
├── employees_50.xlsx
└── README.md
```

## Requirements

- Python 3
- `pandas`
- `openpyxl`

## Installation and Execution

1. Download or clone this repository.
2. Keep `main.py` and `employees_50.xlsx` in the same folder.
3. Open a terminal in that folder.
4. Install the required packages:

   ```bash
   python -m pip install pandas openpyxl
   ```

5. Run the program:

   ```bash
   python main.py
   ```

6. Enter the menu number for the feature you want to test. Choose **7** to exit.

## Data Structures Demonstrated

| Data structure | Use in the project |
|---|---|
| Linked List | Stores and displays transaction records |
| Stack | Demonstrates last-in, first-out transaction display |
| Queue | Processes customers in first-in, first-out order |
| Binary Search Tree | Organizes employee salaries and supports salary search |

## Notes

- The employee features use the sample data in `employees_50.xlsx`. Keep this workbook beside `main.py`.
- Account and transaction data may be stored in memory while the program runs; this is an educational demonstration, not a production banking application.
- Do not upload passwords, API keys, private customer information, or other sensitive data to a public repository.

## Author

**Abhishek Kumar**  
B.Tech CSE AIML – 3D  
SGT University  
Registration No.: 251302219
