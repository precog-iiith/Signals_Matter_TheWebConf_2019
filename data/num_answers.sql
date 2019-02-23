SELECT u.id, count(a.id) as num_answers, sum(a.score) as sum_answer_score from [bigquery-public-data:stackoverflow.posts_answers] a JOIN [bigquery-public-data:stackoverflow.users] u 
on a.owner_user_id=u.id group by u.id;
