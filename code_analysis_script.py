import difflib
import os

# Path to the reference code file in your repository
REFERENCE_CODE_PATH = 'restore_previous_versions_files.py'

# Paths to the cloned repositories
cloned_repo_paths = [
    'https://github.com/Ravi0021/automation.git',
    # 'repo2',
    # Add more paths for additional repositories
]

# List to store code duplication results
duplication_results = []

def analyze_code():
    # Read the reference code file
    with open(REFERENCE_CODE_PATH, 'r') as reference_file:
        reference_code = reference_file.readlines()

    # Iterate over the cloned repositories
    for repo_path in cloned_repo_paths:
        # Read the code files in the repository
        code_files = get_code_files(repo_path)

        # Perform code comparison for each code file
        for code_file in code_files:
            code_file_path = os.path.join(repo_path, code_file)
            with open(code_file_path, 'r') as file:
                code_lines = file.readlines()

            # Perform code comparison using difflib
            similarity_ratio = difflib.SequenceMatcher(None, reference_code, code_lines).ratio()

            # Store the results in the duplication_results list
            duplication_results.append({
                'repository': repo_path,
                'file': code_file,
                'similarity_ratio': similarity_ratio
            })

    # Call the report_results function to generate the report
    report_results()

def get_code_files(repo_path):
    # Provide logic to retrieve the code files within the repository folder
    # This can be done using file system operations or a specific directory structure

    # Example:
    code_folder = os.path.join(repo_path, 'GitHub_Actions')
    code_files = []
    for root, dirs, files in os.walk(code_folder):
        for file in files:
            if file.endswith('.py'):
                code_files.append(os.path.join(root, file))
    return code_files

def report_results():
    # Perform further processing or reporting based on the duplication results
    # You can create issues, send notifications, generate reports, etc.

    # Example: Print the duplication results
    print("Code Duplication Report:")
    for result in duplication_results:
        print(f"Repository: {result['repository']}")
        print(f"File: {result['file']}")
        print(f"Similarity Ratio: {result['similarity_ratio']}")
        print()

# Entry point of the script
if __name__ == '__main__':
    analyze_code()
