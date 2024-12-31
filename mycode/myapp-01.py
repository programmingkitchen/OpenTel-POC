#!/home/ubuntu/.opentel/bin/python

import time
from opentelemetry import context, trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor
# from local_machine_resource_detector import LocalMachineResourceDetector
from common import (
    configure_tracer,
)


""" def configure_tracer(name, version):
    exporter = ConsoleSpanExporter()
    span_processor = BatchSpanProcessor(exporter)
    local_resource = LocalMachineResourceDetector().detect()
    myresource = local_resource.merge(
        Resource.create(
            {
                "service.name": name,
                "service.version": version,
            }
        )
    )
    provider = TracerProvider(resource=myresource)
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer(name, version) """

tracer = configure_tracer("mytracer", "0.0.1")
# logger = configure_logger("grocery-store", "0.1.2")

@tracer.start_as_current_span("snooze")
def snooze(mytime):
    print("+Sleeping for: ", mytime)
    time.sleep(mytime)

@tracer.start_as_current_span("process")
def process():
    print("+Processing")

@tracer.start_as_current_span("browse")
def browse():
    print("+browse(): Browse to website.")
    span = trace.get_current_span()
    span.set_attribute("http.method", "GET")
    snooze(10)
    list()
    process()

@tracer.start_as_current_span("list")
def list():
    print("+list(): List all items")

@tracer.start_as_current_span("display by id")
def display_by_id(id):
    print("+display_by_id(): Display item with ID number.")

@tracer.start_as_current_span("add")
def add(id):
    print("+add(id):  Add id", id)
    print("+add {} to cart".format(id))
    list()

@tracer.start_as_current_span("update")
def update(id):
    print("+update():  Update item", id)
    span = trace.get_current_span()
    span.set_attribute("http.method", "POST")
    snooze(5)

@tracer.start_as_current_span("delete")
def delete(id):
    print("+delete():  Delete item", id)
    list()

# The calls below are not the parent (starts with the method call)
if __name__ == "__main__":
    print("========================================")
    print("STARTING TRACE #1")
    print("========================================")
    browse()

    # This will start a new trace
    print("========================================")
    print("STARTING TRACE #2")
    print("========================================")
    update(100)
   
    




