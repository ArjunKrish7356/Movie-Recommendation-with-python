

def recommend(movie):
    import pandas as pd
    new_df = pd.read_csv('new_df.csv')
    similarity = pd.read_csv('similarity_new.csv')

    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity.iloc[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    item=[]
    for i in movie_list:
        name=new_df.iloc[i[0]]['title']
        item.append(name)
    return item


