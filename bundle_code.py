#!/usr/bin/env python3
import os
import re
from pathlib import Path
from sorted_deps import ClassDependencyAnalyzer

def extract_classes_from_file(file_path):
    """Extract all class definitions from a file using a simple text-based approach."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
        
        # Dictionary to store classes with their full content
        classes = {}
        
        # Track if we're inside a class definition
        inside_class = False
        current_class = None
        class_content = []
        class_indent = None
        
        # Regular expression to match class definition
        class_pattern = re.compile(r'^\s*class\s+(\w+)')
        
        # Process each line
        for line in content:
            if not inside_class:
                # Look for a new class definition
                match = class_pattern.match(line)
                if match:
                    current_class = match.group(1)
                    inside_class = True
                    class_content = [line]
                    class_indent = None  # Will be determined by the first indented line
            else:
                # We're already inside a class
                stripped = line.rstrip()
                
                # If line is empty, just add it and continue
                if not stripped:
                    class_content.append(line)
                    continue
                
                # Get indentation of current line
                current_indent = len(line) - len(line.lstrip())
                
                # If this is the first indented line, record the indentation level
                if class_indent is None and current_indent > 0:
                    class_indent = current_indent
                
                # Check if we've encountered a new top-level statement
                if current_indent == 0:
                    # Check if it's a new class definition
                    match = class_pattern.match(line)
                    if match:
                        # Store previous class
                        classes[current_class] = ''.join(class_content)
                        
                        # Start new class
                        current_class = match.group(1)
                        class_content = [line]
                        class_indent = None
                    else:
                        # Found a non-class top-level statement, end the class
                        classes[current_class] = ''.join(class_content)
                        inside_class = False
                else:
                    # Still inside the class
                    class_content.append(line)
        
        # Don't forget to store the last class if we were tracking one
        if inside_class and current_class:
            classes[current_class] = ''.join(class_content)
        
        return classes
    
    except Exception as e:
        print(f"Error extracting classes from {file_path}: {e}")
        return {}

def extract_external_imports(files):
    """Extract all import statements from files to include in the bundle."""
    try:
        imports = set()
        
        # Regular expressions to match import statements
        import_patterns = [
            re.compile(r'^\s*import\s+(.+)$'),
            re.compile(r'^\s*from\s+(\w+(?:\.\w+)*)\s+import\s+(.+)$')
        ]
        
        # Known modules from the codebase (to exclude)
        local_modules = set(["web", "textual", "data_model", "coordinators"])
        
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                
                for line in content:
                    stripped = line.strip()
                    
                    # Skip comments and empty lines
                    if not stripped or stripped.startswith('#'):
                        continue
                    
                    # Check for import statements
                    for pattern in import_patterns:
                        match = pattern.match(line)
                        if match:
                            # Check if this is an external import
                            if pattern == import_patterns[0]:  # import x
                                module_name = match.group(1).split('.')[0].strip()
                                if module_name not in local_modules:
                                    imports.add(line.rstrip())
                            else:  # from x import y
                                module_name = match.group(1).split('.')[0].strip()
                                if module_name not in local_modules:
                                    imports.add(line.rstrip())
                            break
            except Exception as e:
                print(f"Error processing imports from {file_path}: {e}")
        
        return sorted(list(imports))
    
    except Exception as e:
        print(f"Error extracting external imports: {e}")
        return []

def main():
    # Create analyzer and find all classes
    analyzer = ClassDependencyAnalyzer()
    analyzer.find_all_classes()
    
    # Get classes sorted by dependencies
    sorted_classes = analyzer.get_sorted_classes()
    
    # Get a set of all files containing classes
    all_files = set()
    for class_name in sorted_classes:
        file_path = analyzer.class_to_file.get(class_name)
        if file_path:
            all_files.add(file_path)
    
    # Extract external imports from all files
    external_imports = extract_external_imports(all_files)
    
    # Extract all classes from all files
    all_classes = {}
    for file_path in all_files:
        classes = extract_classes_from_file(file_path)
        all_classes.update(classes)
    
    # Open output file
    with open('tritium_bundle.py', 'w', encoding='utf-8') as outfile:
        # Add header
        outfile.write("#!/usr/bin/env python3\n")
        outfile.write("# This file was automatically generated by bundle_code.py\n\n")
        
        # Add external imports
        outfile.write("# External Imports\n")
        for imp in external_imports:
            outfile.write(f"{imp}\n")
        outfile.write("\n\n")
        
        # Add classes in dependency order
        for class_name in sorted_classes:
            if class_name in all_classes:
                file_path = analyzer.class_to_file.get(class_name, "Unknown")
                outfile.write(f"\n# From {file_path}\n")
                outfile.write(all_classes[class_name])
                outfile.write("\n")
    
    print(f"Bundle complete! Classes bundled to tritium_bundle.py")
    print(f"Bundled {len(sorted_classes)} classes from {len(all_files)} files.")

if __name__ == "__main__":
    main()
