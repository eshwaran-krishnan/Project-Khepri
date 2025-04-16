import os
import sys
import json
import subprocess
import requests
from typing import Dict, List, Union, Optional
from pathlib import Path

def run_command(command: str) -> Dict[str, Union[int, str]]:
    """
    Run a shell command and return the output and exit code.
    
    Args:
        command: Command to execute
        
    Returns:
        Dictionary with stdout, stderr, and exit_code
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": 1
        }

def read_file(file_path: str) -> Dict[str, Union[str, bool]]:
    """
    Read contents from a file.
    
    Args:
        file_path: Path to the file
        
    Returns:
        Dictionary with content and success status
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"content": content, "success": True}
    except Exception as e:
        return {"content": "", "error": str(e), "success": False}

def write_file(file_path: str, content: str, mode: str = 'w') -> Dict[str, bool]:
    """
    Write or append content to a file.
    
    Args:
        file_path: Path to the file
        content: Content to write
        mode: 'w' for write (overwrite), 'a' for append
        
    Returns:
        Dictionary with success status
    """
    try:
        with open(file_path, mode, encoding='utf-8') as f:
            f.write(content)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def append_file(file_path: str, content: str) -> Dict[str, bool]:
    """
    Append content to a file.
    
    Args:
        file_path: Path to the file
        content: Content to append
        
    Returns:
        Dictionary with success status
    """
    return write_file(file_path, content, mode='a')

def web_search(query: str) -> Dict[str, Union[str, bool]]:
    """
    Search the web for information.
    
    Args:
        query: Search query
        
    Returns:
        Dictionary with search results and success status
    """
    try:
        response = requests.get(
            "https://www.googleapis.com/customsearch/v1",
            params={
                "q": query,
                "key": os.environ.get("GOOGLE_API_KEY", ""),
                "cx": os.environ.get("GOOGLE_SEARCH_ENGINE_ID", "")
            }
        )
        return {"results": response.text, "success": True}
    except Exception as e:
        return {"results": "", "error": str(e), "success": False}

def web_fetch(url: str) -> Dict[str, Union[str, bool]]:
    """
    Fetch content from a specific URL.
    
    Args:
        url: URL to fetch content from
        
    Returns:
        Dictionary with content and success status
    """
    try:
        response = requests.get(url)
        return {"content": response.text, "success": True}
    except Exception as e:
        return {"content": "", "error": str(e), "success": False}

def create_project_plan(plan_content: str) -> Dict[str, bool]:
    """
    Create or update the project action plan file.
    
    Args:
        plan_content: Plan content to write
        
    Returns:
        Dictionary with success status
    """
    # Store in a dedicated directory to keep it separate
    plan_dir = Path("project_plan")
    plan_dir.mkdir(exist_ok=True)
    
    plan_file = plan_dir / "action_plan.md"
    
    # Add working directory information
    current_dir = os.getcwd()
    plan_with_dir = f"# Project Action Plan\n\nWorking Directory: {current_dir}\n\n{plan_content}"
    
    return write_file(str(plan_file), plan_with_dir)

def append_to_project_plan(additional_content: str) -> Dict[str, bool]:
    """
    Append content to the project action plan.
    
    Args:
        additional_content: Content to append
        
    Returns:
        Dictionary with success status
    """
    plan_file = Path("project_plan") / "action_plan.md"
    
    # Create the file with working directory if it doesn't exist
    if not plan_file.exists():
        current_dir = os.getcwd()
        initial_content = f"# Project Action Plan\n\nWorking Directory: {current_dir}\n\n"
        write_file(str(plan_file), initial_content)
    
    return append_file(str(plan_file), f"\n{additional_content}")

def read_project_plan() -> Dict[str, Union[str, bool]]:
    """
    Read the current project action plan.
    
    Returns:
        Dictionary with plan content and success status
    """
    plan_file = Path("project_plan") / "action_plan.md"
    return read_file(str(plan_file))

def list_directory(directory: str = ".") -> Dict[str, Union[List[str], bool]]:
    """
    List contents of a directory.
    
    Args:
        directory: Directory path to list (defaults to current directory)
        
    Returns:
        Dictionary with directory contents and success status
    """
    try:
        contents = os.listdir(directory)
        return {"contents": contents, "success": True}
    except Exception as e:
        return {"contents": [], "error": str(e), "success": False}

def get_file_info(file_path: str) -> Dict[str, Union[Dict, bool]]:
    """
    Get information about a file (size, modification time, etc).
    
    Args:
        file_path: Path to the file
        
    Returns:
        Dictionary with file information and success status
    """
    try:
        file_stat = os.stat(file_path)
        info = {
            "size": file_stat.st_size,
            "modified_time": file_stat.st_mtime,
            "created_time": file_stat.st_ctime,
            "is_directory": os.path.isdir(file_path),
            "is_file": os.path.isfile(file_path)
        }
        return {"info": info, "success": True}
    except Exception as e:
        return {"info": {}, "error": str(e), "success": False}

def create_directory(directory_path: str) -> Dict[str, bool]:
    """
    Create a new directory.
    
    Args:
        directory_path: Path of directory to create
        
    Returns:
        Dictionary with success status
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Helper function to convert functions to JSON schema for tool use
def get_functions_schema() -> str:
    """
    Generate a JSON schema of all available functions for the model to use.
    
    Returns:
        JSON string describing all function signatures
    """
    functions = [
        run_command, read_file, write_file, append_file, 
        web_search, web_fetch, create_project_plan, 
        append_to_project_plan, read_project_plan,
        list_directory, get_file_info, create_directory
    ]
    
    schema = []
    for func in functions:
        name = func.__name__
        docstring = func.__doc__ or ""
        schema.append({
            "name": name,
            "description": docstring.strip()
        })
    
    return json.dumps(schema, indent=2)

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
        result = run_command(command)
        print(json.dumps(result, indent=2))
    else:
        print("Available functions:")
        print(get_functions_schema())