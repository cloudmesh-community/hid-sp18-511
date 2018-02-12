from eve import Eve
import platform
import psutil
from flask import jsonify

app = Eve()

#Processor root information
@app.route('/systeminfo')
def getProcessorRootInfo():
    return jsonify("REST API for Processor information")
	
#Processor information
@app.route('/systeminfo/processor')
def getProcessorInfo():
    name = platform.processor()
    return jsonify(name)

#Disk information
@app.route('/systeminfo/disk')
def getDiskInfo():
    return jsonify(psutil.disk_usage('/'))
    
#Memory information
@app.route('/systeminfo/memory')
def getMemoryInfo():
    return jsonify(psutil.virtual_memory())
    
#CPU information
@app.route('/systeminfo/cpu')
def getCPUInfo():
    return jsonify(psutil.cpu_times())
       
if __name__ == '__main__':
	app.run()