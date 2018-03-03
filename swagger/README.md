# Project : Swagger Cloud and Big Data Rest Service

## Purpose :

This REST Service allow user to filter the provided data based on the given critera.
Allowable criterias are filter positive data and filter negative data.
Project can be further enhanced easily based on the customer requirement.
The REST service should conform to Swagger/OpenAPI 2.0 specification. 

## Execution steps for your machine :
* git clone the project
* go to the flaskConnexion directory using `cd`
* Run the following commands one by one:
  * pip install -r requirements.txt
  * python setup.py install
  * python -m swagger_server
* You should see a message like this:
  ``` 
  Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
  ```

## Examples :
```
curl -H "Content-Type: application/json" -X GET -d '{"numbers":"1 2 3 4 -5"}' http://localhost:8080/api/filter?criteria=pos
[
  1,
  2,
  3,
  4
]
```

```
curl -H "Content-Type: application/json" -X GET -d '{"numbers":"1 2 3 4 -5"}' http://localhost:8080/api/filter?criteria=neg
[
  -5
]
```

* When you do not allowed criteria then REST service will return error message
```
curl -H "Content-Type: application/json" -X GET -d '{"numbers":"1 2 3 4 -5"}' http://localhost:8080/api/filter?criteria=test
"provided criteria is not supported"
```

