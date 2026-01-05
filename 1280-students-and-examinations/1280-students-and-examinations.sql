# Write your MySQL query statement below
Select S.student_id, S.student_name, SU.subject_name, Count(E.student_id) as attended_exams
from Students S
Cross Join Subjects SU
Left Join Examinations E
On S.student_id = E.student_id
AND SU.subject_name = E.subject_name
Group by 1,2,3
Order by S.student_id Asc;
