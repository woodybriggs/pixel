import pika, os, time

def pdf_process_function(msg):
  print(" PDF processing")
  print(" [x] Received " + str(msg))
  return

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='fluent') # Declare a queue

# create a function which is called on incoming messages
def callback(ch, method, properties, body):
  pdf_process_function(body)

# set up subscription on the queue
channel.basic_consume('fluent',
  callback,
  auto_ack=True)

# start consuming (blocks)
channel.start_consuming()
connection.close()