# Process Flows
## Smart banking system

## 1. Deposit process
### Description
This process allows a customer to deposit money into a selected bank accont.

## Steps
1. Customer selects an account.
2. System validates that the account exists.
3. Customer enters deposit amount.
4. System validates that the amount is positive.
5. System updates the account balance.
6. System records the transaction in the table of transaction.
7. System confirms successful deposit.

## 2. Withdrawal process
### Description
Withdrawal process allows the user to withdraw money from the account while ensuring that the balance is sufficient.

## Steps
1. Customer selects the desired account.
2. System validates that the account exists.
3. Customer enters withdrawal amount.
4. Systems checks the available amount.
5. If amount is sufficient -> proceed to next step.
6. If amount is insufficient -> reject the transaction.
7. System deducts the withdrawal amount from the available balance.
8. System records the transaction.
9. System confirms that the withdrawal is successful.

## 3. Checking Balance
## Description
This process allows the user to check the balance of the selected account.

## Steps
1. Customer selects the desired account.
2. System validates the account exists.
3. Systems retrieves the account balance.
4. System displays balance.

## 4. Process Flow Summary

| Process    | Column 2                        |
|------------|---------------------------------|
| Deposit    | Amount entered must be positive.|
| Withdrawal | Balance must be sufficient.     |
| Balance    | Account must exist.             |