#!/home/ubuntu/.opentel/bin/python
'''
https://github.com/open-telemetry/opentelemetry-python/issues/3664
'''
import time
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import ConsoleLogExporter, SimpleLogRecordProcessor
from opentelemetry.sdk.resources import Resource

def configure_log_emitter_provider():
    myprovider = LoggerProvider(resource=Resource.create())
    myprovider.add_log_record_processor(SimpleLogRecordProcessor(ConsoleLogExporter()))

def snooze(mytime):
    print("+Sleeping for: ", mytime)
    time.sleep(mytime)

def process():
    print("+Processing")

# Lots of method calls
def browse():
    print("+browse(): Browse to website.")
    snooze(10)
    list()
    process()

def list():
    print("+list(): List all items")

def display_by_id(id):
    print("+display_by_id(): Display item with ID number.")

def add(id):
    print("+add {} to cart".format(id))

def update(id):
    print("+update():  Update item", id)

def delete(id):
    print("+delete():  Delete item", id)

if __name__ == "__main__":
    print("========================================")
    print("STARTING Log #1")
    print("========================================")
    browse()

    




