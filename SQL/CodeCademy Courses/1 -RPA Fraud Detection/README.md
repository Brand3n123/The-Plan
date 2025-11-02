# RPA Fraud Detection (`rpa_project_codecademy.sql`)

## Overview
Codecademy project challenge — identify suspicious transactions in the `transaction_data` table.  
Queries use pattern matching, string filters, and conditional logic to flag possible fraud indicators like fake ZIP codes, joke names, internal IPs, and temp email domains.

---

## Challenge Instructions (from Codecademy)

**Scenario:**

Reputable Product Agency (RPA) has started receiving complaints from their credit card processor about fraudulent transactions. Help your finance department identify potentially risky transactions before they finish processing.

This dataset contains a single table, `transaction_data`.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

---

### **Tasks**

1. **Explore the dataset**  
   Start by getting a feel for the `transaction_data` table.  
   *What are the column names?*

2. **Suspicious ZIP codes**  
   Some fraudulent transactions were recorded as coming from Smokey Bear’s ZIP code (`20252`).  
   Find the `full_names` and `emails` of the transactions listing `20252` as the ZIP code.

3. **Pseudonyms**  
   Fraudsters have used fake names:  
   - `Art Vandelay` for `full_name`, or  
   - added `'der'` as a middle name.  
   Use a query to find the names and emails associated with these transactions.

4. **Invalid IP addresses**  
   Any IP address beginning with `'10.'` is reserved for internal use and should not appear in public traffic.  
   Find the `ip_addresses` and `emails` listed with these transactions.

5. **Temporary email services**  
   Some users made fraudulent transactions using temporary email addresses from services ending with `'temp_email.com'`.  
   Find all `emails` in `transaction_data` with this domain.

6. **Specific transaction search**  
   Finance is looking for a specific transaction.  
   They know:  
   - the IP address starts with `'120.'`  
   - the `full_name` starts with `'John'`  
   Find this transaction.

---


Found result:
| id | full_name | email | zip | ip_address |
|----|------------|-------|-----|-------------|
| 672 | Johnathan Brilleman | jbrillemanin@tinypic.com | 8922 | 120.66.58.128 |



---

## How to Run
In SQLite CLI:
```bash
sqlite3 rpa.db < sql/rpa_project_codecademy.sql