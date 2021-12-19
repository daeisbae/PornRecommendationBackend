from fastapi import FastAPI, Response, status
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pydantic
from typing import List

app = FastAPI()
dataset = pd.read_csv('pornhub.com-db-shrinked1-0-fixed.csv', sep="|")
dataset['categories'] = dataset.categories.str.split(';')
dataset['pornstars'] = dataset.pornstars.str.split(';')
dataset.loc[dataset['categories'].isnull()] = dataset.loc[dataset['categories'].isnull()].apply(lambda x: [])
dataset.loc[dataset['pornstars'].isnull()] = dataset.loc[dataset['pornstars'].isnull()].apply(lambda x: [])
dataset['query'] = dataset['categories'] + dataset['pornstars']
dataset['query'] = dataset['query'].map(lambda x: str(f"\"{str(x)}\""))

def recommendation(dataset, minDuration, maxDuration, minViews, pornstars, categories) -> pd.DataFrame:
    dataset = dataset[(dataset['duration'] >= minDuration) & (dataset['duration'] <= maxDuration) & (dataset['views'] >= minViews)]
    tf_model = TfidfVectorizer(max_features=5000, max_df=0.25, min_df=0.01, stop_words='english')
    tf_matrix = tf_model.fit_transform(dataset['query']).todense()
    tf_df = pd.DataFrame(tf_matrix)
    tf_df.columns = sorted(tf_model.vocabulary_)
    nn = NearestNeighbors(n_neighbors=10, algorithm='ball_tree')
    nn.fit(tf_matrix)
    new = tf_model.transform(pornstars + categories)
    result = nn.kneighbors(new.todense(), return_distance=False)
    prediction = []
    for i in result[1]:
        info = dataset.iloc[i]
        prediction.append({'embed': info['embed'], 'title': info['title'], 'duration': info['duration'],\
             'views': info['views'], 'categories': info['categories'], 'pornstars': info['pornstars'], 'tags': info['tags'],\
                'likes': info['likes'], 'dislikes': info['dislikes'],'thumbnail': info['thumbnail4'].split(';')})
    return prediction


class FilterRequests(pydantic.BaseModel):
    minDuration: int
    maxDuration: int
    minViews: int
    pornstars: List[str]
    categories: List[str]

@app.get("/")
def main():
    return Response(status_code=status.HTTP_200_OK, content="Hello World")

@app.post("/upload", status_code=status.HTTP_201_CREATED)
def upload(response: Response, req: FilterRequests):
    result = None
    try:
        result = recommendation(dataset, req.minDuration, req.maxDuration,\
             req.minViews, req.pornstars, req.categories)
    except Exception as e:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        print(f"Error Occured: {e}\nParameter: {req}")
        return {"message": str(e)}
    return {"message": "success", "result": result}