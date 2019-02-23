import pandas as pd
import numpy as np
import datetime
import string

def combine_google_big_query_results(fnames):
    dataframes = []
    for fname in fnames:
        df_ = pd.read_csv(fname)
        dataframes.append(df_)
    df = pd.concat(dataframes)
    df.to_csv("../data/combined_df.csv")

def augment_df():
    df = pd.read_csv("../data/combined_df.csv")

    column_names = {}
    for column in df:
        new_col_name = column.replace('results_badges_table_', '')
        new_col_name = new_col_name.replace('results_simple_feat_table_', '')
        column_names[column] = new_col_name
    df = df.rename(index=str, columns=column_names)

    df = df.fillna(0)

    df['log_reputation'] = (df['reputation'] + 1).apply(np.log)
    df['log_num_questions'] = (df['num_questions'] + 1).apply(np.log)
    df['log_num_answers'] = (df['num_answers'] + 1).apply(np.log)
    df['log_num_comments'] = (df['num_comments'] + 1).apply(np.log)
    df['log_sum_question_score'] = (df['sum_question_score'] + 1).apply(np.log)
    df['log_sum_answer_score'] = (df['sum_answer_score'] + 1).apply(np.log)
    df['log_sum_comment_score'] = (df['sum_comment_score'] + 1).apply(np.log)
    df['log_up_votes'] = (df['up_votes'] + 1).apply(np.log)
    df['log_down_votes'] = (df['down_votes'] + 1).apply(np.log)

    diff_days = lambda x: (datetime.date.today() - datetime.datetime.strptime(x[:10], '%Y-%m-%d').date()).days

    df['days_since_join'] = df['creation_date'].apply(diff_days)
    df['log_days_since_join'] = (df['days_since_join'] + 1).apply(np.log)

    df['days_since_last_access'] = df['last_access_date'].apply(diff_days)
    df['log_days_since_last_access'] = (df['days_since_last_access'] + 1).apply(np.log)

    df['int_1e6_log_days_since_join'] = (df['log_days_since_join']*1000000).astype(int)
    df['int_1e6_log_days_since_last_access'] = (df['log_days_since_last_access']*1000000).astype(int)

    mean_views = np.mean(list(df['views']))
    stddev_views = np.std(list(df['views']))
    z_score_views = lambda x: ((x - mean_views)/stddev_views)
    df['z_score_views'] = df['views'].apply(z_score_views)

    mean_impact = np.mean(list(df['impact']))
    stddev_impact = np.std(list(df['impact']))
    z_score_impact = lambda x: ((x - mean_impact)/stddev_impact)
    df['z_score_impact'] = df['impact'].apply(z_score_impact)

    df.to_csv("../data/augmented_combined_df.csv")
