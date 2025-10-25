class Card:
    def __init__(self, card_type, card_no, cvv, expiry_date, balance=()):
        self.card_type = card_type
        self.card_no = card_no
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.balance = balance

    def display_info(self):
        self.card_type = input("Card Type")
        self.card_no = input("Card Number")
        self.cvv = input("CVV")
        self.expiry_date = input("Expiration Date")
        self.balance = input("Balance")

class Customer:
    def __init__(self, cid, cname, acc_number, phone, emailID, balance=()):
        self.cid = cid
        self.cname = cname
        self.acc_no = acc_number
        self.phone = phone
        self.emailID = emailID
        self.balance = balance
        self.credit_card = ()
        self.debit_card =()
    def display_info(self):
        self.cid = input("Customer ID")
        self.cname = input("Custommer Name")
        self.acc_no = input("Account Number")
        self.phone = input("Phone Number")
        self.emailID = input("Email ID")
        self.balance = input("Balance")
        self.credit_card = ()
        self.debit_card = ()

    def transfer_funds(self, other_customer, amount):
        if amount <= self.balance:
            self.balance = amount
            other_customer.balance = amount
            print("(amount) transferred from (...) to (...)")
        else:
            print("negative balance")

customers = []
cards = []

while True:
    print("Main Menu")
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer Funds Between Customers")
    print("4. Assign Card to Customer")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Commit")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        cid = input("Enter Customer ID: ")
        cname = input("Enter Customer Name: ")
        acc_no = input("Enter Account No: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        bal = input("Enter Initial Balance: ")
        customers.append(Customer(cid, cname, acc_no, phone, email, bal))
        print("Customer created")

    elif choice == '2':
        card_type = input("Enter Card Type:")
        card_no = input("Enter Card Number:")
        cvv = input("Enter CVV:")
        expiry = input("Enter Expiration Date:")
        bal = input("Enter Card Balance:")
        cards.append(Card(card_type, card_no, cvv, expiry, bal))
        print("Card created")

    elif choice == '3':
        if (customers) < 2:
            print("2 customers are required for transfer")
        else:
            for self in(customers):
                print("(i, c cname?)")
            from_id = int(input("Transfer From (...):"))
            to_id = int(input("Transfer to (...): "))
            amount = input("Enter Amount:")
            customers[from_id].transfer_funds(customers[to_id], amount)

    elif choice == '4':
        if not customers or cards:
            print("create customers and cards")
        else:
            for self in(customers):
                print("c.cname")
            cust_id = int(input("select customer:"))
            for self in (cards):
                print("(card.card_no) (card.card_type)")
            card_id = int(input("Select Card:"))
            selected_card = cards[card_id]
            if selected_card.card_type == 'debit':
                customers[cust_id].debit_card = selected_card
            else:
                customers[cust_id].credit_card.append(selected_card)
            print("caed assigned")

    elif choice == '5':
        for c in customers:
            c.display_info()

    elif choice == '6':
        for card in cards:
            card.display_info()

    elif choice == '7':
        print("Commiting")

    elif choice == '8':
        print("Exiting program")
        break

    else:
        print("Invalid")
