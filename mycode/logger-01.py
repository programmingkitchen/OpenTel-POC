#!/home/ubuntu/.opentel/bin/python
'''
https://github.com/open-telemetry/opentelemetry-python/issues/3664

Can we generate logs without an emitter?

'''
import time
import logging.config
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import ConsoleLogExporter, SimpleLogRecordProcessor
from opentelemetry.sdk.resources import Resource

# Configure 1. provider, 2. processor, 3.exporter. 
# What happened to the emitter?
def configure_log_provider():
    myprovider = LoggerProvider(resource=Resource.create())
    myexporter = ConsoleLogExporter()
    myprovider.add_log_record_processor(SimpleLogRecordProcessor(myexporter))
    return myprovider

def configure_logging(logger_provider):
    logging.config.dictConfig({
    "version": 1,
    "formatters": {
        "simple": {"format": "%(name)s [%(module)s.%(lineno)s]: %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "simple",
            "class": "opentelemetry.sdk._logs.LoggingHandler",
            "logger_provider": logger_provider,
        }
    },
    "loggers": {
        "__main__": {"handlers": ["console"], "level": "INFO"},
    }
})

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
    myprovider = configure_log_provider()
    configure_logging(myprovider)
    logging.getLogger().info("Test Log")


    




