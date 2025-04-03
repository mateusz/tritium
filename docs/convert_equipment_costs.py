import csv
import os

def convert_csv_to_markdown():
    # Define input and output file paths
    input_file = "docs/equipment_costs.csv"
    output_file = "docs/equipment_costs.md"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found")
        return
    
    # Read CSV and convert to markdown
    with open(input_file, 'r') as csv_file, open(output_file, 'w') as md_file:
        csv_reader = csv.reader(csv_file)
        
        # Read header row
        headers = next(csv_reader)
        
        # Define resource columns (all columns after Factory)
        resource_columns = headers[4:]
        
        # Process each row
        for row in csv_reader:
            item_id = row[0]
            item_name = row[1]
            tech_level = row[2]
            factory = row[3]
            
            # Extract resources with values > 0
            resources = []
            for i, resource_name in enumerate(resource_columns):
                try:
                    resource_value = int(row[i + 4])
                    if resource_value > 0:
                        resources.append(f"{resource_value} {resource_name}")
                except (ValueError, IndexError):
                    # Skip if value is not a number or index is out of range
                    continue
            
            # Write item to markdown
            md_file.write(f"- {item_name}:\n")
            md_file.write(f"  - RequiredRank: {tech_level}\n")
            md_file.write(f"  - RequiredLocation: {factory}\n")
            
            # Write cost if there are resources
            if resources:
                md_file.write(f"  - Cost: {', '.join(resources)}\n")
            
    print(f"Conversion complete! Output saved to {output_file}")

if __name__ == "__main__":
    convert_csv_to_markdown()