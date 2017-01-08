import argparse
import time

import pika
import sys

def publish(data, r_key):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	# channel.exchange_declare(exchange='topic_logs',type='topic')

	# routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
	routing_key = r_key
	message = "{}".format(data)

	# using a default exchange '' means only the routing key is used to identify the path (direct!)
	channel.basic_publish(exchange='',
		              routing_key=routing_key,
		              body=message)
	print(" [x] Sent %r:%r" % (routing_key, message))
	connection.close()

print('Start Investment Period')

# specify optional argument, set default to 3
parser = argparse.ArgumentParser()
parser.add_argument("--interval", type=int, default=3, help="display a square of a given number")

# get the values of the parameters
args = parser.parse_args()
# print("Interval set to: {}".format(args.interval))

# risky values based on the clarification page of the assignment
# riskyasset = [100, 102, 105, 110, 115, 115, 115, 117, 120, 119, 116, 116, 116, 114, 118, 120, 125, 130, 123, 119, 116, 115, 114, 113, 120]
# risky values based on table from cppi presentation
riskyasset = [100, 105, 103, 96, 93, 97, 103, 108, 112, 100, 104]


template = '{"price":"XXX"}'

# iterate over the risky asset, send it to the message queue, sleep the defined period
for r in riskyasset:
	message = template.replace('XXX', str(r))
	print (message)
	publish(message, 'spring-boot')
	time.sleep(args.interval)

print("End Investment Period.")


