import ast
from pushToChromaDB import push_to_chromadb

# Global JSON structure
codebase = {
    "files": {},
    "dependencies": [],
    "indexes": {
        "class_names": {},
        "function_names": {},
        "imports": {}
    }
}

def parse_python_file(codebase ,file_path: str):
    """
    Parse a Python file and update the global codebase JSON structure.
    """
    with open(file_path, "r") as f:
        file_content = f.read()

    # Parse the file content into an AST
    tree = ast.parse(file_content, filename=file_path)

    # Initialize file-specific data
    file_data = {
        "classes": [],
        "functions": [],
        "imports": []
    }

    # Create custom visitor to avoid processing nested functions multiple times
    class CodeVisitor(ast.NodeVisitor):
        def __init__(self):
            self.current_class = None
            self.processed_functions = set()

        def visit_ClassDef(self, node):
            # Process class definition
            class_id = f"{file_path}#{node.name}"
            class_info = {
                "id": class_id,
                "name": node.name,
                "methods": [],
                "inherits": [base.id for base in node.bases if isinstance(base, ast.Name)],
                "docstring": ast.get_docstring(node)
            }
            
            # Process class code
            class_code = ast.unparse(node)
            push_to_chromadb(class_code, node.name, file_path)
            
            # Process methods
            self.current_class = class_id
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    self.visit_FunctionDef(item, is_method=True)
            self.current_class = None
            
            file_data["classes"].append(class_info)
            codebase["indexes"]["class_names"].setdefault(node.name, []).append(class_id)
            self.generic_visit(node)

        def visit_FunctionDef(self, node, is_method=False):
            if node in self.processed_functions:
                return
                
            self.processed_functions.add(node)
            
            if is_method:
                function_id = f"{self.current_class}.{node.name}"
            else:
                function_id = f"{file_path}#{node.name}"

            function_info = {
                "id": function_id,
                "name": node.name,
                "parameters": [arg.arg for arg in node.args.args],
                "return_type": None,
                "calls": [],
                "docstring": ast.get_docstring(node)
            }

            function_code = ast.unparse(node)
            push_to_chromadb(function_code, node.name, file_path)

            if not is_method:
                file_data["functions"].append(function_info)
                codebase["indexes"]["function_names"].setdefault(node.name, []).append(function_id)

            self.generic_visit(node)

    visitor = CodeVisitor()
    visitor.visit(tree)

    # Process imports separately
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                import_info = {
                    "module": alias.name,
                    "imported_items": [],
                    "is_from_import": False,
                    "alias": alias.asname
                }
                file_data["imports"].append(import_info)
                codebase["indexes"]["imports"].setdefault(alias.name, []).append(file_path)
        elif isinstance(node, ast.ImportFrom):
            import_info = {
                "module": node.module,
                "imported_items": [alias.name for alias in node.names],
                "is_from_import": True,
                "alias": None
            }
            file_data["imports"].append(import_info)
            codebase["indexes"]["imports"].setdefault(node.module, []).append(file_path)

    # Add file data to the global codebase
    codebase["files"][file_path] = file_data