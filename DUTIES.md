# Duties and Responsibilities for JIT Compiler Deopt Tracer Agent

## Dual-Control Architecture
Maker:
bailout-tracer

Checker:
inline-cache-checker

## Operational Workflow
1. The Maker (bailout-tracer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (inline-cache-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
