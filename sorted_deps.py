import os
import ast
import networkx as nx
from pathlib import Path

# Directories to analyze
DIRS_TO_ANALYZE = ["web", "textual", "data_model", "coordinators"]

class ClassDependencyAnalyzer:
    def __init__(self):
        self.class_to_file = {}  # Maps class names to their file paths
        self.module_to_classes = {}  # Maps module paths to class names defined in them
        self.dependency_graph = nx.DiGraph()
        self.class_dependencies = {}  # Maps each class to its direct dependencies
        
    def find_all_classes(self):
        """Analyze all files in the specified directories to build the dependency graph."""
        # First pass: collect all classes and their module paths
        self._collect_classes()
        
        # Second pass: analyze imports to determine dependencies
        self._analyze_imports()
    
    def _collect_classes(self):
        """Find all class definitions and record which module they're in."""
        for directory in DIRS_TO_ANALYZE:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        self._extract_classes_from_file(file_path)
    
    def _extract_classes_from_file(self, file_path):
        """Extract all class definitions from a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            tree = ast.parse(code)
            
            # Convert file path to module path (for import resolution)
            module_path = self._file_to_module_path(file_path)
            
            # Find all class definitions
            classes = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_name = node.name
                    classes.append(class_name)
                    self.class_to_file[class_name] = file_path
                    self.dependency_graph.add_node(class_name)
                    self.class_dependencies[class_name] = set()  # Initialize empty dependency set
            
            # Store classes defined in this module
            if classes:
                self.module_to_classes[module_path] = classes
                
        except Exception as e:
            print(f"Error extracting classes from {file_path}: {e}")
    
    def _file_to_module_path(self, file_path):
        """Convert a file path to its corresponding module path."""
        parts = file_path.split(os.path.sep)
        # Find the start of the module path
        start_idx = 0
        for i, part in enumerate(parts):
            if part in DIRS_TO_ANALYZE:
                start_idx = i
                break
        
        # Build the module path
        module_parts = parts[start_idx:]
        # Replace .py with nothing for the last part
        if module_parts and module_parts[-1].endswith('.py'):
            module_parts[-1] = module_parts[-1][:-3]
        
        return '.'.join(module_parts)
    
    def _analyze_imports(self):
        """Analyze import statements in all files to build the dependency graph."""
        for directory in DIRS_TO_ANALYZE:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        self._analyze_file_imports(file_path)
    
    def _analyze_file_imports(self, file_path):
        """Analyze import statements in a file to find dependencies."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            tree = ast.parse(code)
            
            # Get classes defined in this file
            classes_in_file = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes_in_file.append(node.name)
            
            # Find all import statements
            for node in ast.walk(tree):
                # Regular imports (import X)
                if isinstance(node, ast.Import):
                    for name in node.names:
                        imported_module = name.name
                        self._process_import(imported_module, None, classes_in_file)
                
                # From imports (from X import Y)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        module_name = node.module
                        for name in node.names:
                            imported_name = name.name
                            self._process_import(module_name, imported_name, classes_in_file)
        
        except Exception as e:
            print(f"Error analyzing imports in {file_path}: {e}")
    
    def _process_import(self, module_name, imported_name, classes_in_file):
        """Process an import statement to find class dependencies."""
        # If importing a specific name, check if it's a class
        if imported_name:
            # Check if the imported name is a known class
            if imported_name in self.class_to_file:
                # All classes in this file depend on the imported class
                for class_in_file in classes_in_file:
                    # Add edge: imported_class -> class_in_file (meaning class_in_file depends on imported_class)
                    self.dependency_graph.add_edge(imported_name, class_in_file)
                    # Record this dependency for debugging
                    self.class_dependencies[class_in_file].add(imported_name)
        
        # Check if importing a module containing classes
        for potential_module, classes in self.module_to_classes.items():
            # If the import matches or is a parent of the potential module
            if potential_module == module_name or potential_module.startswith(module_name + '.'):
                # All classes in this file depend on all classes in the imported module
                for imported_class in classes:
                    for class_in_file in classes_in_file:
                        if imported_class != class_in_file:  # Avoid self-dependencies
                            # Add edge: imported_class -> class_in_file
                            self.dependency_graph.add_edge(imported_class, class_in_file)
                            # Record this dependency for debugging
                            self.class_dependencies[class_in_file].add(imported_class)
    
    def get_sorted_classes(self):
        """Return classes sorted by their dependencies.
        
        Classes at the beginning of the list are dependencies for classes later in the list.
        """
        try:
            # Use topological sort to get classes in dependency order
            sorted_classes = list(nx.topological_sort(self.dependency_graph))
            return sorted_classes
        except nx.NetworkXUnfeasible:
            print("Error: Circular dependencies detected. Using approximate sort.")
            # Fall back to a simple heuristic if there are cycles
            return sorted(self.dependency_graph.nodes(), 
                          key=lambda n: self.dependency_graph.in_degree(n) - self.dependency_graph.out_degree(n))
    
    def get_dependencies_for_class(self, class_name):
        """Get the list of classes that the given class depends on."""
        if class_name in self.class_dependencies:
            return self.class_dependencies[class_name]
        return set()
    
    def find_cycles(self):
        """Find and return all cycles in the dependency graph."""
        try:
            return list(nx.simple_cycles(self.dependency_graph))
        except nx.NetworkXNoCycle:
            return []

def main():
    analyzer = ClassDependencyAnalyzer()
    analyzer.find_all_classes()
    
    sorted_classes = analyzer.get_sorted_classes()
    
    print("Classes sorted by dependencies:")
    for i, class_name in enumerate(sorted_classes, 1):
        file_path = analyzer.class_to_file.get(class_name, "Unknown")
        dependencies = analyzer.get_dependencies_for_class(class_name)
        if dependencies:
            dependencies_str = ", ".join(sorted(dependencies))
            print(f"{i}. {class_name} - {file_path} - Depends on: {dependencies_str}")
        else:
            print(f"{i}. {class_name} - {file_path} - No dependencies")
    
    # Print cycles in the dependency graph
    cycles = analyzer.find_cycles()
    if cycles:
        print("\nCircular dependencies detected:")
        for i, cycle in enumerate(cycles, 1):
            # Format the cycle as Class1 -> Class2 -> Class3 -> Class1
            cycle_str = " -> ".join(cycle)
            cycle_str += f" -> {cycle[0]}"
            print(f"Cycle {i}: {cycle_str}")
            
            # Print file paths for classes in the cycle
            print("  File paths:")
            for class_name in cycle:
                file_path = analyzer.class_to_file.get(class_name, "Unknown")
                print(f"    {class_name}: {file_path}")
    else:
        print("\nNo circular dependencies detected.")
    
    # Optionally, visualize the graph if pydot is installed
    try:
        from networkx.drawing.nx_pydot import write_dot
        write_dot(analyzer.dependency_graph, "class_dependencies.dot")
        print("\nDependency graph saved to class_dependencies.dot")
        print("To visualize: 'dot -Tpng class_dependencies.dot -o class_dependencies.png'")
    except ImportError:
        print("\nInstall pydot to visualize the dependency graph: pip install pydot")

if __name__ == "__main__":
    main() 