SWAGGER_CODEGEN=java -jar swagger-codegen-cli-2.3.1.jar 
YAML_FILE=filter.yaml
DEST_DIR=server/

clean:
	if [ -d $(DEST_DIR) ]; then rm -r $(DEST_DIR); fi
        
service: 
	sh download-swagger-codegen.sh
	$(SWAGGER_CODEGEN) generate -i $(YAML_FILE) -l python-flask -o $(DEST_DIR) -D supportPython3=true
	cp default_controller.py $(DEST_DIR)/swagger_server/controllers
	cp filter_util.py $(DEST_DIR)/swagger_server
	cd $(DEST_DIR) && pip install -r requirements.txt && \
	python setup.py install

start: 
	cd $(DEST_DIR) && python -m swagger_server

stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

test:
	curl -H "Content-Type: application/json" -X GET -d '{"elements":"ab abc abcde"}' http://localhost:8080/cloudmesh/filter/regex?criteria=ab
	curl -H "Content-Type: application/json" -X GET -d '{"elements":"ab abc abcde"}' http://localhost:8080/cloudmesh/filter/regex?criteria=ab.
	curl -H "Content-Type: application/json" -X GET -d '{"elements":"ab abc abcde"}' http://localhost:8080/cloudmesh/filter/regex?criteria=ab*

container:
	sudo docker build --no-cache -t cloudmesh-filter .
	sudo docker run -p 8080:8080 cloudmesh-filter
