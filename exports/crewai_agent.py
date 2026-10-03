from crewai import Agent

jit_compiler_deopt_tracer = Agent(
    role="Jit Compiler Deopt Tracer",
    goal="Deliver high-precision autonomous Jit Compiler Deopt Tracer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
