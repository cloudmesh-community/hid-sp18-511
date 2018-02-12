from eve import Eve
from flask import jsonify
from computer import Computer
import psutil

app = Eve()
Computer = Computer()

#Processor root information
@app.route('/computer')
def getProcessorRootInfo():
    return jsonify("REST API for computer information")
	
#Processor information
@app.route('/computer/processor')
def getProcessorInfo():    
    return jsonify(Computer.name)

#Disk information
@app.route('/computer/disk')
def getDiskInfo():
    return jsonify(Computer.disk_usage)	
    
#Memory information
@app.route('/computer/memory')
def getMemoryInfo():
    return jsonify(Computer.virtual_memory)
    
#CPU information
@app.route('/computer/cpu')
def getCPUInfo():
    return jsonify(Computer.cpu_times)
       
if __name__ == '__main__':
	app.run()