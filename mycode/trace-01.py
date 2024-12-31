#!/usr/bin/env python3

import time
from opentelemetry import context, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor

def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = BatchSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer("trace-01.py", "0.0.1")

def snooze(mytime):
    print("+Sleeping for: ", mytime)
    time.sleep(mytime)

def browse():
     print("+login(): Browse to website.")
     snooze(10)
     list()

def list():
    print("+list(): List all items")

def display_by_id(id):
    print("+display_by_id(): Display item with ID number.")

def add(id):
    print("+add(id):  Add id", id)
    list()

def update(id):
    print("+update():  Update item", id)
    list()

def delete(id):
    print("+delete():  Delete item", id)
    list()

tracer = configure_tracer()

if __name__ == "__main__":
   
    with tracer.start_as_current_span("Visit site"):
        browse()




