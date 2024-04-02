-- group number by score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
