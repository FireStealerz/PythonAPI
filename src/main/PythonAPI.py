from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


app = FastAPI()

my_posts = [{ "title" : "Post1", "content": "Content1", "ID": 0}, {"title": "Post2", "content": "Content2", "ID": 1}]


@app.api_route('/', methods=['GET', 'HEAD', 'DELETE'])

class PostSchema(BaseModel):
    title: str
    content : str
    published: bool = True
   

def find_post(id):
    for p in my_posts:
        if p["ID"] == id:
         return p 

def find_index(id):
    for i, p in enumerate(my_posts):
        if p["ID"] == id:
            return i



@app.get("/")
async def root():
    return {"mesage": "Hello World"}
engine = create_engine(f'mysql+pymysql://{USER}:{PASSWD}@localhost/{DB}')
Base.metadata.create_all(engine)
@app.get("/posts")
async def get_posts():
    return{"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def createposts(post : PostSchema):
    new_post=post.dict()
    new_post["ID"] = randrange(2, 1000000)
    my_posts.append(new_post)
    return{"data" : new_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    post = find_index(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with ID:{id} doesn`t exist!")
    my_posts.pop(post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with ID:{id} doesn`t exist!")Top 10 IPs visitadas
        #response.status_code = status.HTTP_404_NOT_FOUND
          # return {"message": f"Post with ID:{id} doesn`t exist!"}
    return{"post": post}

@app.put("/posts/{id}")
async def update_post(id: int, post: PostSchema):
    new_post = find_index(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Post with ID:{id} doesn`t exist!")
    post2 = post.dict()
    my_posts[new_post] = post2
    return{"Message": "Post updated"}    



#works top down
##it gets the first matching def
## /posts/latest after posts/{id} will get posts/{id} always