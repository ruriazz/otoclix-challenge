# Otoclix Recruitment Challenge
##  Simple API to manage blog posts of blog
live demo available at https://otoclix-challenge.herokuapp.com/posts

#### GET : Get Posts

```
https://otoclix-challenge.herokuapp.com/posts
```

#### GET : Show Post

```
https://otoclix-challenge.herokuapp.com/posts/<ID_POST>
```

#### POST : Create Post

```
https://otoclix-challenge.herokuapp.com/posts
```
with data body
````
{
    "title": "TITLE_OF_CONTENT | maxlength=200",
    "content": "CONTENT | maxlength=300"
}
````

#### PUT : Update Post

```sh
https://otoclix-challenge.herokuapp.com/posts/<ID_POST>
```
with data body
````
{
    "title": "TITLE_OF_CONTENT | maxlength=200",
    "content": "CONTENT | maxlength=300"
}
````

#### DEL : Delete Post

```sh
https://otoclix-challenge.herokuapp.com/posts/<ID_POST>
```