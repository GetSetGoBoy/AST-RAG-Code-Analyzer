# QA Report: RAG Accuracy Experiment

The system was evaluated using two primary methods: unit testing via `qa_test.py` and integration testing via `my_tool.py` against a real-world logic file.

#### 1. RAG Accuracy Test (`qa_test.py`)

This test validates the engine's ability to map vulnerable code patterns to the correct security recommendations in the knowledge base.

| Test Case (Input) | Expected Keyword in Advice | Result |
| --- | --- | --- |
| `eval(data)` | `ast.literal_eval` | PASS |
| `password = '123'` | `Environment Variables` |  PASS |
| `strcpy(a, b)` | `strncpy` |  PASS |
| `innerHTML` | `textContent` |  PASS |

**Accuracy Score: 100%**

#### 2. Integration Test (`app_logic.py`)

The linter was run against `app_logic.py` to test its ability to identify naming, complexity, and security issues simultaneously.

**Issues Detected in `app_logic.py`:**

* **[NAMING]** Line 4: `db` is flagged for being too short.
* **[COMPLEXITY]** Line 7: `sync_patient_data` flagged for having > 5 arguments (8 total).
* **[SECURITY]** Line 9: `eval()` usage detected with AI Advice: *“Use ast.literal_eval() for safety.”*
* **[SECURITY]** Line 13: Hardcoded `db_password` detected.
