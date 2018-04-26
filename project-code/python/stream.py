import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)
    # Create a local StreamingContext with two working thread and batch interval of 1 second
	sc = SparkContext("local[2]", "NetworkWordCount")
	ssc = StreamingContext(sc, 1)
	
	# Create a DStream that will connect to hostname:port, like localhost:9999
	# Firewalls might block this!
	lines = ssc.socketTextStream("localhost", 9999)
	
	# Split each line into words
	words = lines.flatMap(lambda line: line.split(" "))
	
	# Count each word in each batch
	pairs = words.map(lambda word: (word, 1))
	wordCounts = pairs.reduceByKey(lambda x, y: x + y)

	# Print the first ten elements of each RDD generated in this DStream to the console
	wordCounts.pprint()

    ssc.start()
    ssc.awaitTermination()