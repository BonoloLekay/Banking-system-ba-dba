-- SAMPLE DATA

-- Insert sample data in customers table
INSERT INTO Customers (customer_id, name, surname, email)
VALUES
(1, 'John', 'Doe', 'john.doe@email.com'),
(2, 'Sarah', 'Mokoena', 'sarah.mokoena@email.com');

-- Insert sample data in accounts table
INSERT INTO Accounts (account_id, customer_id, balance)
VALUES
(101, 1, 1500.00),
(102, 2, 2500.00);

-- Insert sample data in transactions table
INSERT INTO Transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
VALUES
(1001, 101, 'Deposit', 500.00, '2026-04-30 10:00:00'),
(1002, 102, 'Withdrawal', 200.00, '2026-04-30 11:00:00');