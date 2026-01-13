# AST-code-Analyzer
A static analysis tool that uses AST parsing to audit Python code for security risks, naming issues, and structural complexity. It provides instant terminal feedback to ensure enterprise-grade code quality and safety in ERP and medical systems.

# Features
AST-Based Analysis: Understands code structure rather than just searching for text.

Security Guardrails: Detects dangerous eval() calls to prevent injection attacks.

Quality Control: Identifies poor naming conventions (short function names).

Complexity Check: Flags functions with excessive arguments to promote clean code.

# How It Works
The tool uses Python's Abstract Syntax Tree (AST) module to parse source code into a logical tree. It "visits" specific nodes—like function definitions and call expressions—comparing them against predefined safety and style rules without actually executing the code.

# How to Run
python my_tool.py app_logic.py
