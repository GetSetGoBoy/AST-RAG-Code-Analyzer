# AST-RAG-Code-Analyzer
AST-RAG-Code-Analyzer is an AI-powered static code analysis tool that bridges the gap between traditional linting and modern LLM intelligence. By combining Abstract Syntax Tree (AST) parsing with a Retrieval-Augmented Generation (RAG) engine, it not only identifies structural flaws but also retrieves context-specific security advice from a curated knowledge base. This hybrid approach ensures that developers receive precise, expert-level recommendations for fixing vulnerabilities in real-time.

# Features
Hybrid Analysis Engine: Combines deterministic AST-based pattern matching with probabilistic AI-driven retrieval for 100% accuracy in detection and high-quality advice.

Context-Aware Advice (RAG): Unlike generic linters, it retrieves specific documentation and "why-to-fix" explanations from a customizable security knowledge base.

Vectorized Search: Uses HuggingFace Embeddings to convert security rules into mathematical vectors, allowing the tool to find advice based on "meaning" rather than just keywords.

Zero-Overhead Security: Operates entirely on your local machine using a persistent ChromaDB store, ensuring your source code never leaves your environment.

Extensible Knowledge Base: Easily update the tool’s "intelligence" by simply adding new rules to a plain text file—no retraining of AI models required.

# How It Works
Parsing (The X-Ray): The tool reads the target Python file and builds a "Tree" of its structure (AST).

Detection: It traverses the tree, looking for specific "Nodes" like function definitions (to check naming), arguments (to check complexity), and sensitive function calls (like eval).

Retrieval: When a security risk is found, a query is sent to the RAG Engine.

Vector Matching: The engine converts the query into an embedding and performs a similarity search against the ChromaDB vector store to find the best-matching security rule.

Reporting: The tool outputs a clean, color-coded report showing the line number, the issue type, and the "AI Advice" retrieved from the knowledge base.

# How to Run
Prerequisites
Ensure you have Python installed and the following libraries:

python -m pip install langchain-chroma langchain-huggingface sentence-transformers

Step 1: Setup the Knowledge Base
Before the first run, you must let the "Librarian" read your rules.

python -c "import rag_engine; rag_engine.build_knowledge_base()"

Step 2: Run the Analyzer
Execute the tool against any Python file (e.g., app_logic.py) to see the results.

python my_tool.py app_logic.py

Step 3: Update Rules (Optional)
If you want to add new security rules, simply edit security_knowledge.txt and repeat Step 1. The tool will immediately "learn" the new rules.

# Quality Assurance (QA)
The Security RAG Linter has been rigorously audited using a automated testing suite to ensure the advice provided is technically accurate and relevant to the detected vulnerabilities.

#### Performance Metrics

Verified Accuracy: The RAG system was audited using the "Context Quality Experiment" protocol via qa_test.py.

Results: Achieved a 5/5 accuracy score on core technical queries (including eval, strcpy, and innerHTML).

Audit Logic: Each test case compares the RAG engine's output against a list of required security keywords (e.g., ensuring ast.literal_eval is recommended for eval()).

#### Integration Testing

The system was further validated by running my_tool.py against app_logic.py, successfully identifying:

Naming Issues: Short variable/function names.

Functional Complexity: Excessive argument counts.

Security Flaws: Hardcoded secrets and dangerous function calls.

Full Report: For a detailed breakdown of the testing methodology and individual test results, please view the QA Report.md.
