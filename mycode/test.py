#!/usr/bin/env python3

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
    print("+Browse(): (rjg)")

def process():
    print("+Process() (rjg)")

if __name__ == "__main__":
    tracer = configure_tracer()
    span1 = tracer.start_span("SPAN #1")
    ctx = trace.set_span_in_context(span1)
    token = context.attach(ctx)
    span2 = tracer.start_span("SPAN #2")
    browse()
    process()
    span2.end()
    context.detach(token)
    span1.end()


