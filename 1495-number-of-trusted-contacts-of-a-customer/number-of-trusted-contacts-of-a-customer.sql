# Write your MySQL query statement below
SELECT a.invoice_id,
    b.customer_name,
    price,
    COUNT(c.contact_email)contacts_cnt,
    COUNT(d.email)trusted_contacts_cnt
FROM Invoices a
JOIN Customers b
ON a.user_id = b.customer_id
LEFT JOIN Contacts c
ON b.customer_id = c.user_id
LEFT JOIN Customers d
ON c.contact_email = d.email
GROUP BY 1,2,3
ORDER BY 1