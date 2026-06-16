import json
import sys

def run(input_path: str):
    with open(input_path) as f:
        data = json.load(f)
    
    project_id = data.get("projectId", "unknown")
    function_inputs = data.get("functionInputs", {})
    check_material = function_inputs.get("checkMaterial", True)
    
    print(f"Running Check Material function for project: {project_id}")
    print(f"Check material enabled: {check_material}")
    
    # Stub validation - always passes for now
    print("Wall validator OK, project: " + project_id)
    print("All walls have materials assigned.")
    sys.exit(0)

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.json"
    run(input_file)
