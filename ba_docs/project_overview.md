- # Bank Management System

# 1. Executive Summary

The purpose of this project is to design and simulatee a banking system that allows the management of customers, accounts, and financial transactions. The system aims to improve data accuracy and ensure transactional integrity while providing structured financial record-keeping using relational database and application layer.

# 2. Business Problem

Manual banking record systems can lead to inaccurate transaction tracking, data duplication, and inconsistent account balances. This makes it difficult to reliably manage customer financial data and maintain transaction history.

A structured system is required because it ensures accurate, consistent, and traceable management of customer accounts and financial transactions.

# 3. Business Objectives

## The system must achieve the following:

- Ensure accurate and real-time transaction recording
- Maintain consistent customer and account data
- Provide reliable account balance tracking
- Enable efficient retrieval of financial history
- Support decision-making through structured data

# 4. Stakeholders

| Stakeholder          | Role                               |
| -------------------- | ---------------------------------- |
| Customer             | Performs deposits and withdrawals  |
| Bank Staff           | Manages accounts and transactions  |
| System Administrator | Maintains database and system      |
| Business Analyst     | Reviews financial data and reports |

# 5. System Scope

## In Scope:

- Customer profile management
- Account creation and management
- Deposit and withdrawal processing
- Transaction recording
- Balance inquiries

## Out of Scope:

- Online/mobile banking interface
- External payment gateway integration
- Real-time banking integration
- Fraud detection systems (future enhancement)

# 6. Functional Requiremnts

## The system must be able to:

- Create and manage customer profiles
- Open and manage bank accounts
- Process deposits and withdrawals
- Record all financial transactions
- Display account balances
- Retrieve transaction history per account

# 7. Non-functional requirements

- Data Integrity: All transactions must be accurate and consistent
- Reliability: System must ensure no data loss during operations
- Performance: Queries must execute efficiently
- Maintainability: Code and database must be structured clearly

# 8. Business Rules

- A customer may own multiple accounts
- Each account is linked to one customer only
- Withdrawals cannot exceed available balance
- Every transaction must be recorded in the system
- Account balance must reflect all transactions accurately

# 9. Assumptions

- The system is a simulation for educational purposes
- No real banking systems or live financial data are used
- Users are manually inserted
- Database is hosted locally on MySQL environment

# 10. Success Criteria

## The system will be considered successful if:

- Transactions correctly update account balances
- All operations are recorded in the transaction table
- No invalid withdrawals are allowed
- Data remains consistent across all tables.
- SQL queries return accurate and expected results.
- The system structure is well documented and organised.

## Conclusion

This project demonstrates foundational skills in Business Analysis and Database Design through a simulated banking system. It serves as a portfolio project showcasing readiness for graduate-level opportunities in IT and data-related roles.
