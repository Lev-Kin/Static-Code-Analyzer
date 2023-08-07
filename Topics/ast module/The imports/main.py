import ast

class ImportVisitor(ast.NodeVisitor):
    def visit_Import(self, node):
        for alias in node.names:
            print(alias.name)

tree = ast.parse(code)
import_visitor = ImportVisitor()
import_visitor.visit(tree)
