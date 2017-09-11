-- Problem: Given a table "cinema", 

-- Return: Please write a SQL query to output movies with an odd numbered ID and a description that is not 'boring'. Order the result by rating. 

# Write your MySQL query statement below
SELECT id,movie,description,rating
FROM cinema
WHERE (id%2) = 1 AND description != 'boring'
ORDER BY rating DESC
