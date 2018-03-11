SWAGGER_CODEGEN=java -jar ~/swagger/swagger-codegen-cli -2.3.1.jar
YAML_FILE=filter.yaml
DEST_DIR=server/

dest:
	mkdir $(DEST_DIR)

service: dest
	$(SWAGGER_CODEGEN) generate -i $(YAML_FILE) -l python-flask -o $(DESTDIR) -D supportPython3=true
	cp -r *.py $(DEST_DIR)/swagger_server/controllers
	cd $(DEST_DIR) && pip install -r requirements.txt && \
        python setup.py install

start: 
	cd $(DEST_DIR) && python -m swagger_server

test:
	echo "Regression test start"
	curl -H "Content-Type: application/json" -X GET -d '{"numbers":"1 2 3 4 -5"}' http://localhost:8080/api/filter?criteria=pos
    curl -H "Content-Type: application/json" -X GET -d '{"numbers":"1 2 3 4 -5"}' http://localhost:8080/api/filter?criteria=neg
    curl -H "Content-Type: application/json" -X GET -d '{"numbers":"1 2 3 4 -5"}' http://localhost:8080/api/filter?criteria=test           
	echo "Regression test complete"
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -r $(DEST_DIR)


