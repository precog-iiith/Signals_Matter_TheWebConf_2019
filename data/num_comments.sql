SELECT u.id, count(c.user_id) as num_comments, sum(score) as sum_comment_score from [bigquery-public-data:stackoverflow.comments] c JOIN [bigquery-public-data:stackoverflow.users] u 
on c.user_id=u.id group by u.id;
