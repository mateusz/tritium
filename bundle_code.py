import os
import re

# Directories to scan
directories = [
    "data_model",
    "coordinators",
    "textual",
    "web"
]

# Main output file
output_file = "tritium_bundle.py"

# Dictionary to store module content
modules = {}

# Function to clean up imports
def clean_imports(content, module_path):
    # Replace relative imports with absolute imports
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip empty lines or comments
        if not line.strip() or line.strip().startswith('#'):
            cleaned_lines.append(line)
            continue
        
        # Handle various import patterns
        if re.match(r'^from\s+\.\.?[.\w]*\s+import', line) or re.match(r'^import\s+\.', line):
            # Skip relative imports as we'll consolidate everything
            continue
        elif re.match(r'^from\s+(data_model|coordinators|textual|cli|web)\s+import', line) or re.match(r'^import\s+(data_model|coordinators|textual|cli|web)', line):
            # Skip project-specific imports as we'll consolidate everything
            continue
        else:
            # Keep external imports
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

# Function to scan directory and get all Python files
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                module_path = file_path.replace('/', '.').replace('\\', '.').replace('.py', '')
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Clean up imports
                    cleaned_content = clean_imports(content, module_path)
                    
                    # Store content
                    modules[module_path] = {
                        'path': file_path,
                        'content': cleaned_content
                    }
                    print(f"Processed: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

# Function to sort modules in dependency order
def sort_modules():
    # Simple approach: put __init__ files first, then move data_model before coordinators before textual/cli/web
    sorted_modules = {}
    
    # First: all __init__ files
    for module, data in modules.items():
        if module.endswith('__init__'):
            sorted_modules[module] = data
    
    # Second: data_model files (non-init)
    for module, data in modules.items():
        if 'data_model' in module and not module.endswith('__init__'):
            sorted_modules[module] = data
    
    # Third: coordinators files (non-init)
    for module, data in modules.items():
        if 'coordinators' in module and not module.endswith('__init__'):
            sorted_modules[module] = data
    
    # Fourth: cli files
    for module, data in modules.items():
        if 'cli' in module and not module.endswith('__init__'):
            sorted_modules[module] = data
            
    # Fifth: web files
    for module, data in modules.items():
        if 'web' in module and not module.endswith('__init__'):
            sorted_modules[module] = data
            
    # Sixth: textual files (non-init)
    for module, data in modules.items():
        if 'textual' in module and not module.endswith('__init__'):
            sorted_modules[module] = data
    
    # Finally: any remaining files
    for module, data in modules.items():
        if module not in sorted_modules:
            sorted_modules[module] = data
    
    return sorted_modules

# Function to process web_interface.py separately to maintain compatibility
def process_web_interface():
    web_interface_path = "web/interface.py"
    if os.path.exists(web_interface_path):
        try:
            with open(web_interface_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Get only the essential parts needed for the web interface
            # This is specific to the project's structure
            return content
        except Exception as e:
            print(f"Error processing web interface: {str(e)}")
            return ""
    return ""

# Function to write the combined file
def write_combined_file(sorted_modules):
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("""#!/usr/bin/env python3
# Tritium Game - Bundled Version
# This file is auto-generated and contains all game code combined into a single file.

""")
        
        # Write external imports (only once)
        external_imports = set()
        for module, data in sorted_modules.items():
            content = data['content']
            for line in content.split('\n'):
                if line.startswith('import ') or line.startswith('from '):
                    if not any(proj_dir in line for proj_dir in ['data_model', 'coordinators', 'textual', 'cli', 'web', '.']):
                        external_imports.add(line)
        
        for imp in sorted(external_imports):
            f.write(f"{imp}\n")
        
        f.write("\n\n# ========== START OF BUNDLED CODE ==========\n\n")
        
        # Write each module's content
        for module, data in sorted_modules.items():
            path = data['path']
            content = data['content']
            
            # Skip imports as we've handled them
            content_without_imports = '\n'.join([line for line in content.split('\n') 
                                              if not (line.startswith('import ') or 
                                                     line.startswith('from '))])
            
            f.write(f"\n# ===== Module: {path} =====\n")
            f.write(content_without_imports)
            f.write("\n\n")
        
        # Write launcher code
        f.write("""
# ========== END OF BUNDLED CODE ==========

# Launcher code
if __name__ == "__main__":
    # Web mode check
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--web":
        # For web mode
        try:
            from web.interface import WebInterface
            from textual.game_runner import start_game as start_game_internal
            
            def start_game():
                return start_game_internal(interface_type='web')
                
            result = start_game()
            print(result)
        except Exception as e:
            print(f"Error starting web game: {str(e)}")
    else:
        # For CLI mode
        try:
            from cli.interface import CliInterface
            from textual.game_runner import start_game as start_game_internal
            
            def start_game():
                return start_game_internal(interface_type='cli')
                
            result = start_game()
            print(result)
        except Exception as e:
            print(f"Error starting CLI game: {str(e)}")
""")

# Main execution
def main():
    print(f"Starting bundling process to create {output_file}...")
    
    # Scan all directories
    for directory in directories:
        scan_directory(directory)
    
    # Sort modules
    sorted_modules = sort_modules()
    
    # Write combined file
    write_combined_file(sorted_modules)
    
    print(f"Completed! All code has been bundled into {output_file}")
    print(f"Total modules processed: {len(modules)}")

if __name__ == "__main__":
    main() 