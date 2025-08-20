# Write your MySQL query statement below
SELECT ST.student_id, 
    ST.student_name, 
    SU.subject_name, 
    IFNULL(COUNT(Ex.student_id),0) AS attended_exams
FROM Students ST
CROSS JOIN Subjects SU
LEFT JOIN Examinations Ex
    ON SU.subject_name = Ex.subject_name
    AND ST.student_id = Ex.student_id
GROUP BY ST.student_id, ST.student_name, SU.subject_name
ORDER BY student_id, subject_name
