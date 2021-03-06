from string import punctuation
from sklearn.feature_extraction import stop_words
stopwords = stop_words.ENGLISH_STOP_WORDS




def remove_first_last_quote(dataframe, col):
    dataframe[col] = dataframe[col].str[1:-1]
    return dataframe

def split_df_col_text_by_delim(df, col, delim=" "):
    df[col] = df[col].str.split(delim)
    return df

def merge_user_posts_into_string(df, col, delim = "\|\|\|"):
    df[col] = df[col].str.replace(delim, " ")
    return df

def group_type_posts(df, type_col, text_col):
    return df.groupby(type_col)[text_col].apply(lambda x: "%s" % ', '.join(x)).reset_index()

def create_post_length_list(dataframe, col, newcol):
    dataframe[newcol] = ""
    for i in range(len(dataframe.index)):
        char_count_list = []
        for post in range(len(dataframe[col][i])):
            char_count_list.append(len(dataframe[col][i][post]))
        dataframe[newcol][i] = char_count_list
    return dataframe

def group_post_length_lists_by_type(df, type_col, list_col):
    df2 = df.groupby(type_col).agg({list_col: 'sum'})
    return df2

def to_lowercase(df, col):
    df[col] = df[col].str.lower()
    return  df

def remove_punctuation(text, punctuation = punctuation):
    return ''.join([char for char in text if char not in punctuation])

def splt_text_by_delim(text, delim = " "):
    return text.split(delim)

def remove_stopword_custom(word_list, common_stopwords, custom_stopwords = []):
    stopword_set = common_stopwords + custom_stopwords
    return [word for word in word_list if word not in stopword_set]

    