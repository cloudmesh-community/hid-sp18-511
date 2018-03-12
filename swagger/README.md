# Project : Swagger Cloud and Big Data Rest Service

## Purpose :

This REST Service allow user to filter the provided numbers based on the given critera.
Allowable criterias are filter positive numbers and filter negative numbers.
Project can be further enhanced easily based on the customer requirement.
The REST service should conform to Swagger/OpenAPI 2.0 specification. 

## Execution steps for your machine :
* git clone the project
* Run the service on the host machine 
     * make clean
     * make service
     * make start 
     * You should see a message like this:
     ``` 
     Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
     ``` 
 * Stop the service on the host machine
     * make stop     
 * Test the service on the host machine
     * make test
 * cleaup directories on the host machine
     * make clean
 * Run the service on container
     * make container
     * You should see a message like this:
     ``` 
     Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
     ```

## Test Examples :
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

