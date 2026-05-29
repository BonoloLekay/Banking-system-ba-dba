USE banking_db;

DROP PROCEDURE IF EXISTS Deposit;

DELIMITER $$

CREATE PROCEDURE Deposit (
    IN p_account_id INT,
    IN p_amount DECIMAL(10,2)
)
BEGIN
    UPDATE accounts
    SET balance = balance + p_amount
    WHERE account_id = p_account_id;
END$$

DELIMITER ;

