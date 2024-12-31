#!/usr/bin/env python3

from opentelemetry import trace
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
    print("+Browse(): call browse (rjg)")

if __name__ == "__main__":
    tracer = configure_tracer()
    span = tracer.start_span("This is the name of the span (rjg)")
    browse()
    span.end()