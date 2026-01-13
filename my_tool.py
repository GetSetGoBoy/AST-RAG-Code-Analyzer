import ast
import sys

class CodeLinter(ast.NodeVisitor):
    def __init__(self):
        self.issue_count = 0

    def visit_FunctionDef(self, node):
        if len(node.name) < 3:
            print(f"🚩 [NAMING] Line {node.lineno}: '{node.name}' is too short.")
            self.issue_count += 1
        
        if len(node.args.args) > 5:
            print(f"🚩 [COMPLEXITY] Line {node.lineno}: '{node.name}' has too many arguments ({len(node.args.args)}).")
            self.issue_count += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'eval':
            print(f"⚠️ [SECURITY] Line {node.lineno}: 'eval()' detected. Risk in medical systems!")
            self.issue_count += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                name_lower = target.id.lower()
                if "password" in name_lower or "secret" in name_lower:
                    print(f"❌ [SECURITY] Line {node.lineno}: Hardcoded '{target.id}' detected!")
                    self.issue_count += 1
        self.generic_visit(node)

def run_demo():
    if len(sys.argv) < 2:
        print("Please provide a file name.")
        return
    filename = sys.argv[1]
    with open(filename, "r") as f:
        code = f.read()
    tree = ast.parse(code)
    print(f"\n--- Checking {filename} for your Internship Demo ---")
    checker = CodeLinter()
    checker.visit(tree)
    print(f"\nAnalysis Finished. Total Issues: {checker.issue_count}\n")

if __name__ == "__main__":
    run_demo()