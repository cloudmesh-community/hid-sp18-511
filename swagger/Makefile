SWAGGER_CODEGEN=java -jar ~/swagger/swagger-codegen-cli-2.3.1.jar
YAML_FILE=filter.yaml
DEST_DIR=server/

dest:
	mkdir $(DEST_DIR)

service: 
	$(SWAGGER_CODEGEN) generate -i $(YAML_FILE) -l python-flask -o $(DEST_DIR) -D supportPython3=true
	cp default_controller.py $(DEST_DIR)/swagger_server/controllers
	cp filter_util.py $(DEST_DIR)/swagger_server
	cd $(DEST_DIR) && pip install -r requirements.txt && \
	python setup.py install


start: 
	cd $(DEST_DIR) && python -m swagger_server


stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -r $(DEST_DIR)
