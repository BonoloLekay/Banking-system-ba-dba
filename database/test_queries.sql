-- Checking all data
SELECT * FROM customers;
SELECT * FROM accounts;
SELECT * FROM transactions;

-- Account relationships
-- Customer 
SELECT 
    c.customer_id,
    c.name,
    a.account_id,
    a.balance
FROM customers c
JOIN accounts a 
ON c.customer_id = a.customer_id;

-- Account
SELECT 
    a.account_id,
    t.amount,
    t.transaction_date
FROM Accounts a
JOIN Transactions t 
ON a.account_id = t.account_id;

-- Checking balance
SELECT 
    account_id,
    balance
FROM Accounts;

-- Filtering
SELECT * 
FROM Transactions
WHERE transaction_type = 'Deposit';

-- Checking total transactions per account
SELECT 
    account_id,
    COUNT(*) AS total_transactions
FROM Transactions
GROUP BY account_id;

-- Check balance for each account
SELECT 
    c.name,
    SUM(a.balance) AS total_balance
FROM Customers c
JOIN Accounts a 
ON c.customer_id = a.customer_id
GROUP BY c.name;