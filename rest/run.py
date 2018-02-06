from eve import Eve
import platform
import psutil
from flask import jsonify

app = Eve()

#Processor information
@app.route('/processor')
def getProcessorInfo():
    name = platform.processor()
    return jsonify(name)

#Disk information
@app.route('/disk')
def getDiskInfo():
    return jsonify(psutil.disk_usage('/'))
    
#Memory information
@app.route('/memory')
def getMemoryInfo():
    return jsonify(psutil.virtual_memory())
    
#CPU information
@app.route('/cpu')
def getCPUInfo():
    return jsonify(psutil.cpu_times())
       
if __name__ == '__main__':
	app.run()