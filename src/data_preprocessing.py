import pandas as pd

def load_data():
    """Load raw product and review files of Kaggle"""

    df_product = pd.read_csv('data\product_info.csv')
    df_r1 = pd.read_csv('data\reviews_0-250.csv')
    df_r2 = pd.read_csv('data\reviews_250-500.csv')
    df_r3 = pd.read_csv('data\reviews_500-750.csv')
    df_r4 = pd.read_csv('data\reviews_750-1250.csv')
    df_r5 = pd.read_csv('data\reviews_1250-end.csv')
    df_reviews = pd.concat([df_r1,df_r2,df_r3,df_r4,df_r5],axis=0)
    return df_product,df_reviews

def drop_high_null_columns(df,threshold=0.7):
    """Drop columns with more than threshold % missing values."""

    null_ratio = df.isnull().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index
    return df.drop(columns=cols_to_drop)

def merge_dfs(df_product,df_reviews):
    """Merge product and review dfs"""
    return pd.merge(df_reviews,df_product,on='product_id',how='left')

def load_processedDfs():
    """Load, clean and merge data"""
    df_reviews, df_product = load_data()
    df_reviews = drop_high_null_columns(df_reviews,threshold=0.7)
    df_product = drop_high_null_columns(df_product,threshold=0.7)
    df_merged = merge_dfs(df_product,df_reviews)

    # renaming merged columns with same name
    rename_cols = {'product_name_x':'product_name',
                   'brand_name_x':'brand_name',
                   'rating_x':'product_rating',
                   'rating_y':'review_rating',
                   'price_usd_x':'price_usd',
                   }
    df_merged = df_merged.rename(columns=rename_cols)
    # dropping index and duplicate columns
    drop_cols = ['Unnamed: 0','product_name_y','brand_name_y','price_usd_y']
    df_merged = df_merged.drop(columns=drop_cols)
    return df_merged
