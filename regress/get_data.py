import pandas as pd
import sys

def get_data(filepath):
    df = pd.read_csv(filepath)
    df['inc_per_filer'] = df.AGI/df.num_returns
    df['inc_per_capita'] = df.AGI/df.people
    df['clinton_win'] = 0
    df.loc[df.clinton>df.trump,'clinton_win'] = 1 # set up target variable
    test_cols = df.columns[8:-1]
    y_var = df.clinton_win
    test_df = df[test_cols]
    id_df = df[df.columns[:8]]
    id_df['winner'] = 'Trump'
    id_df.loc[df.index[clinton_win ==1], 'winner'] = "Clinton"
    return id_df, test_df, y_var

if __name__=="__main__":
    get_data(sys.argv[1])
