SELECT u.id, count(q.id) as num_questions from [bigquery-public-data:stackoverflow.posts_questions] q JOIN [bigquery-public-data:stackoverflow.users] u 
on q.owner_user_id=u.id group by u.id;
