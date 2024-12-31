#!/usr/bin/env python3

import time
from opentelemetry import context, trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = SimpleSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(span_processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer("test.py", "0.0.1")

def browse():
    print("+Browse()")

def process():
    print("+Process()")

def test():
    print("+Test()")

def snooze(mytime):
    print("+Sleeping for: ", mytime)
    time.sleep(mytime)

# Why is the context only attached to Span 1?  Span 2 is "inside span #1"
if __name__ == "__main__":
    tracer = configure_tracer()

    # Start span 1 (parent) which takes a while
    span1 = tracer.start_span("SPAN #1")
    test()
    snooze(15)
    ctx = trace.set_span_in_context(span1)
    token = context.attach(ctx)

    # Start span #2 which runs quickly
    span2 = tracer.start_span("SPAN #2")
    browse()
    process()
    browse()
    span2.end()
    context.detach(token)
    span1.end()

    span3 = tracer.start_span("SPAN #3")
    print("========================================")
    snooze(15)
    span3.end()


