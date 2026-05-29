USE banking_db;

DROP PROCEDURE IF EXISTS Deposit;

DELIMITER $$

CREATE PROCEDURE Deposit (
    IN p_account_id INT,
    IN amount DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance + p_amount
    WHERE account_id = p_account_id;

    INSERT INTO transactions(account_id, transaction_type, amount, transaction_date)
    VALUES (p_account_id, 'DEPOSIT', p_amount, NOW());

    COMMIT;
END$$

DELIMITER ;

DROP PROCEDURE IF EXISTS Withdraw;
DELIMITER //

CREATE PROCEDURE withdraw(
    IN p_account_id INT,
    IN p_amount DECIMAL(10,2)
)
BEGIN
    DECLARE current_balance DECIMAL(10,2);

    -- Get current balance
    SELECT balance
    INTO current_balance
    FROM accounts
    WHERE account_id = p_account_id;

    -- Check if sufficient funds exist
    IF current_balance >= p_amount THEN

        UPDATE accounts
        SET balance = balance - p_amount
        WHERE account_id = p_account_id;

        INSERT INTO transactions (
            account_id,
            transaction_type,
            amount,
            transaction_date
        )
        VALUES (
            p_account_id,
            'WITHDRAW',
            p_amount,
            NOW()
        );

        COMMIT;

    ELSE
        ROLLBACK;
    END IF;

END //

DELIMITER ;