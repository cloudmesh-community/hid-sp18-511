# Project : Swagger Cloud and Big Data Rest Service

## Purpose :

This REST Service allow user to filter the data based on the given regular expression critera.
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
curl -H "Content-Type: application/json" -X GET -d '{"elements":"ab abc abcde"}' http://localhost:8080/cloudmesh/filter/regex?criteria=ab
[
  "ab",
  "abc",
  "abcde"
]
```

```
curl -H "Content-Type: application/json" -X GET -d '{"elements":"ab abc abcde"}' http://localhost:8080/cloudmesh/filter/regex?criteria=ab.
[
  "abc",
  "abcde"
]
```

```
curl -H "Content-Type: application/json" -X GET -d '{"elements":"ab abc abcde"}' http://localhost:8080/cloudmesh/filter/regex?criteria=ab*
[
  "ab",
  "abc",
  "abcde"
]
```
