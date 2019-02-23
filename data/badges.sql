SELECT
  user_id,
  COUNT(CASE
      WHEN name="Altruist" THEN 1 END) AS num_Altruist_badges, COUNT(CASE
      WHEN name="Benefactor" THEN 1 END) AS num_Benefactor_badges,
  COUNT(CASE
      WHEN name="Curious" THEN 1 END) AS num_Curious_badges, COUNT(CASE
      WHEN name="Inquisitive" THEN 1 END) AS num_Inquisitive_badges,
  COUNT(CASE
      WHEN name="Socratic" THEN 1 END) AS num_Socratic_badges, COUNT(CASE
      WHEN name="Favorite Question" THEN 1 END) AS num_Favorite_Question_badges,
  COUNT(CASE
      WHEN name="Stellar Question" THEN 1 END) AS num_Stellar_Question_badges, COUNT(CASE
      WHEN name="Investor" THEN 1 END) AS num_Investor_badges,
  COUNT(CASE
      WHEN name="Nice Question" THEN 1 END) AS num_Nice_Question_badges, COUNT(CASE
      WHEN name="Good Question" THEN 1 END) AS num_Good_Question_badges,
  COUNT(CASE
      WHEN name="Great Question" THEN 1 END) AS num_Great_Question_badges, COUNT(CASE
      WHEN name="Popular Question" THEN 1 END) AS num_Popular_Question_badges,
  COUNT(CASE
      WHEN name="Notable Question" THEN 1 END) AS num_Notable_Question_badges, COUNT(CASE
      WHEN name="Famous Question" THEN 1 END) AS num_Famous_Question_badges,
  COUNT(CASE
      WHEN name="Promoter" THEN 1 END) AS num_Promoter_badges, COUNT(CASE
      WHEN name="Scholar" THEN 1 END) AS num_Scholar_badges,
  COUNT(CASE
      WHEN name="Student" THEN 1 END) AS num_Student_badges, COUNT(CASE
      WHEN name="Tumbleweed" THEN 1 END) AS num_Tumbleweed_badges,
  COUNT(CASE
      WHEN name="Enlightened" THEN 1 END) AS num_Enlightened_badges, COUNT(CASE
      WHEN name="Explainer" THEN 1 END) AS num_Explainer_badges,
  COUNT(CASE
      WHEN name="Refiner" THEN 1 END) AS num_Refiner_badges, COUNT(CASE
      WHEN name="Illuminator" THEN 1 END) AS num_Illuminator_badges,
  COUNT(CASE
      WHEN name="Generalist" THEN 1 END) AS num_Generalist_badges, COUNT(CASE
      WHEN name="Guru" THEN 1 END) AS num_Guru_badges,
  COUNT(CASE
      WHEN name="Nice Answer" THEN 1 END) AS num_Nice_Answer_badges, COUNT(CASE
      WHEN name="Good Answer" THEN 1 END) AS num_Good_Answer_badges,
  COUNT(CASE
      WHEN name="Great Answer" THEN 1 END) AS num_Great_Answer_badges, COUNT(CASE
      WHEN name="Populist" THEN 1 END) AS num_Populist_badges,
  COUNT(CASE
      WHEN name="Reversal" THEN 1 END) AS num_Reversal_badges, COUNT(CASE
      WHEN name="Revival" THEN 1 END) AS num_Revival_badges,
  COUNT(CASE
      WHEN name="Necromancer" THEN 1 END) AS num_Necromancer_badges, COUNT(CASE
      WHEN name="Self-Learner" THEN 1 END) AS num_Self_Learner_badges,
  COUNT(CASE
      WHEN name="Teacher" THEN 1 END) AS num_Teacher_badges, COUNT(CASE
      WHEN name="Tenacious" THEN 1 END) AS num_Tenacious_badges,
  COUNT(CASE
      WHEN name="Unsung Hero" THEN 1 END) AS num_Unsung_Hero_badges, COUNT(CASE
      WHEN name="Autobiographer" THEN 1 END) AS num_Autobiographer_badges,
  COUNT(CASE
      WHEN name="Caucus" THEN 1 END) AS num_Caucus_badges, COUNT(CASE
      WHEN name="Constituent" THEN 1 END) AS num_Constituent_badges,
  COUNT(CASE
      WHEN name="Commentator" THEN 1 END) AS num_Commentator_badges, COUNT(CASE
      WHEN name="Pundit" THEN 1 END) AS num_Pundit_badges,
  COUNT(CASE
      WHEN name="Enthusiast" THEN 1 END) AS num_Enthusiast_badges, COUNT(CASE
      WHEN name="Fanatic" THEN 1 END) AS num_Fanatic_badges,
  COUNT(CASE
      WHEN name="Mortarboard" THEN 1 END) AS num_Mortarboard_badges, COUNT(CASE
      WHEN name="Epic" THEN 1 END) AS num_Epic_badges,
  COUNT(CASE
      WHEN name="Legendary" THEN 1 END) AS num_Legendary_badges, COUNT(CASE
      WHEN name="Precognitive" THEN 1 END) AS num_Precognitive_badges,
  COUNT(CASE
      WHEN name="Beta" THEN 1 END) AS num_Beta_badges, COUNT(CASE
      WHEN name="Quorum" THEN 1 END) AS num_Quorum_badges,
  COUNT(CASE
      WHEN name="Convention" THEN 1 END) AS num_Convention_badges, COUNT(CASE
      WHEN name="Talkative" THEN 1 END) AS num_Talkative_badges,
  COUNT(CASE
      WHEN name="Outspoken" THEN 1 END) AS num_Outspoken_badges, COUNT(CASE
      WHEN name="Yearling" THEN 1 END) AS num_Yearling_badges,
  COUNT(CASE
      WHEN name="Analytical" THEN 1 END) AS num_Analytical_badges, COUNT(CASE
      WHEN name="Announcer" THEN 1 END) AS num_Announcer_badges,
  COUNT(CASE
      WHEN name="Booster" THEN 1 END) AS num_Booster_badges, COUNT(CASE
      WHEN name="Publicist" THEN 1 END) AS num_Publicist_badges,
  COUNT(CASE
      WHEN name="Census" THEN 1 END) AS num_Census_badges, COUNT(CASE
      WHEN name="Informed" THEN 1 END) AS num_Informed_badges,
  COUNT(CASE
      WHEN name="Not a Robot" THEN 1 END) AS num_Not_a_Robot_badges, COUNT(CASE
      WHEN name="Documentation Beta" THEN 1 END) AS num_Documentation_Beta_badges,
  COUNT(CASE
      WHEN name="Documentation Pioneer" THEN 1 END) AS num_Documentation_Pioneer_badges, COUNT(CASE
      WHEN name="Documentation User" THEN 1 END) AS num_Documentation_User_badges,
  COUNT(CASE
      WHEN name="Citizen Patrol" THEN 1 END) AS num_Citizen_Patrol_badges, COUNT(CASE
      WHEN name="Deputy" THEN 1 END) AS num_Deputy_badges,
  COUNT(CASE
      WHEN name="Marshall" THEN 1 END) AS num_Marshall_badges, COUNT(CASE
      WHEN name="Civic Duty" THEN 1 END) AS num_Civic_Duty_badges,
  COUNT(CASE
      WHEN name="Cleanup" THEN 1 END) AS num_Cleanup_badges, COUNT(CASE
      WHEN name="Constable" THEN 1 END) AS num_Constable_badges,
  COUNT(CASE
      WHEN name="Sheriff" THEN 1 END) AS num_Sheriff_badges, COUNT(CASE
      WHEN name="Critic" THEN 1 END) AS num_Critic_badges,
  COUNT(CASE
      WHEN name="Custodian" THEN 1 END) AS num_Custodian_badges, COUNT(CASE
      WHEN name="Reviewer" THEN 1 END) AS num_Reviewer_badges,
  COUNT(CASE
      WHEN name="Steward" THEN 1 END) AS num_Steward_badges, COUNT(CASE
      WHEN name="Disciplined" THEN 1 END) AS num_Disciplined_badges,
  COUNT(CASE
      WHEN name="Editor" THEN 1 END) AS num_Editor_badges, COUNT(CASE
      WHEN name="Strunk & White" THEN 1 END) AS num_Strunk_White_badges,
  COUNT(CASE
      WHEN name="Copy Editor" THEN 1 END) AS num_Copy_Editor_badges, COUNT(CASE
      WHEN name="Electorate" THEN 1 END) AS num_Electorate_badges,
  COUNT(CASE
      WHEN name="Excavator" THEN 1 END) AS num_Excavator_badges, COUNT(CASE
      WHEN name="Archaeologist" THEN 1 END) AS num_Archaeologist_badges,
  COUNT(CASE
      WHEN name="Organizer" THEN 1 END) AS num_Organizer_badges, COUNT(CASE
      WHEN name="Peer Pressure" THEN 1 END) AS num_Peer_Pressure_badges,
  COUNT(CASE
      WHEN name="Proofreader" THEN 1 END) AS num_Proofreader_badges, COUNT(CASE
      WHEN name="Sportsmanship" THEN 1 END) AS num_Sportsmanship_badges,
  COUNT(CASE
      WHEN name="Suffrage" THEN 1 END) AS num_Suffrage_badges, COUNT(CASE
      WHEN name="Supporter" THEN 1 END) AS num_Supporter_badges,
  COUNT(CASE
      WHEN name="Synonymizer" THEN 1 END) AS num_Synonymizer_badges, COUNT(CASE
      WHEN name="Tag Editor" THEN 1 END) AS num_Tag_Editor_badges,
  COUNT(CASE
      WHEN name="Research Assistant" THEN 1 END) AS num_Research_Assistant_badges, COUNT(CASE
      WHEN name="Taxonomist" THEN 1 END) AS num_Taxonomist_badges,
  COUNT(CASE
      WHEN name="Vox Populi" THEN 1 END) AS num_Vox_Populi_badges
FROM
  [bigquery-public-data:stackoverflow.badges] 
GROUP BY
  user_id;
