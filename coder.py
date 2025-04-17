from typing import Any, Dict, List, Union
import httpx
from mcp.server.fastmcp import FastMCP
from tools import (
    run_command, read_file, write_file, append_file, 
    web_search, web_fetch, create_project_plan, 
    append_to_project_plan, read_project_plan,
    list_directory, get_file_info, create_directory
)

# Initialize FastMCP server
mcp = FastMCP("coder")

@mcp.tool()
async def execute_command(command: str) -> Dict[str, Union[int, str]]:
    """
    Execute a shell command and return the output and exit code.
    
    Args:
        command (str): The shell command to execute
        
    Returns:
        Dict[str, Union[int, str]]: Dictionary containing:
            - stdout (str): Standard output from the command
            - stderr (str): Standard error from the command
            - exit_code (int): Command exit code (0 for success)
    """
    return run_command(command)

@mcp.tool()
async def read_file_content(file_path: str) -> Dict[str, Union[str, bool]]:
    """
    Read contents from a file.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        Dict[str, Union[str, bool]]: Dictionary containing:
            - content (str): File contents if successful
            - success (bool): True if read was successful
            - error (str): Error message if unsuccessful
    """
    return read_file(file_path)

@mcp.tool()
async def write_file_content(file_path: str, content: str, mode: str = 'w') -> Dict[str, bool]:
    """
    Write or append content to a file.
    
    Args:
        file_path (str): Path to the file
        content (str): Content to write
        mode (str, optional): 'w' for write (overwrite), 'a' for append. Defaults to 'w'
        
    Returns:
        Dict[str, bool]: Dictionary containing:
            - success (bool): True if write was successful
            - error (str): Error message if unsuccessful
    """
    return write_file(file_path, content, mode)

@mcp.tool()
async def append_to_file(file_path: str, content: str) -> Dict[str, bool]:
    """
    Append content to a file.
    
    Args:
        file_path (str): Path to the file
        content (str): Content to append
        
    Returns:
        Dict[str, bool]: Dictionary containing:
            - success (bool): True if append was successful
            - error (str): Error message if unsuccessful
    """
    return append_file(file_path, content)

@mcp.tool()
async def search_web(query: str) -> Dict[str, Union[str, bool]]:
    """
    Search the web for information using Google Custom Search API.
    
    Args:
        query (str): Search query string
        
    Returns:
        Dict[str, Union[str, bool]]: Dictionary containing:
            - results (str): Search results in JSON format
            - success (bool): True if search was successful
            - error (str): Error message if unsuccessful
    """
    return web_search(query)

@mcp.tool()
async def fetch_url(url: str) -> Dict[str, Union[str, bool]]:
    """
    Fetch content from a specific URL.
    
    Args:
        url (str): URL to fetch content from
        
    Returns:
        Dict[str, Union[str, bool]]: Dictionary containing:
            - content (str): Fetched content
            - success (bool): True if fetch was successful
            - error (str): Error message if unsuccessful
    """
    return web_fetch(url)

@mcp.tool()
async def create_plan(plan_content: str) -> Dict[str, bool]:
    """
    Create or update the project action plan file.
    
    Args:
        plan_content (str): Content to write to the plan file
        
    Returns:
        Dict[str, bool]: Dictionary containing:
            - success (bool): True if plan creation was successful
            - error (str): Error message if unsuccessful
    """
    return create_project_plan(plan_content)

@mcp.tool()
async def append_plan(additional_content: str) -> Dict[str, bool]:
    """
    Append content to the project action plan.
    
    Args:
        additional_content (str): Content to append to the plan
        
    Returns:
        Dict[str, bool]: Dictionary containing:
            - success (bool): True if append was successful
            - error (str): Error message if unsuccessful
    """
    return append_to_project_plan(additional_content)

@mcp.tool()
async def read_plan() -> Dict[str, Union[str, bool]]:
    """
    Read the current project action plan.
    
    Returns:
        Dict[str, Union[str, bool]]: Dictionary containing:
            - content (str): Plan content if successful
            - success (bool): True if read was successful
            - error (str): Error message if unsuccessful
    """
    return read_project_plan()

@mcp.tool()
async def list_dir(directory: str = ".") -> Dict[str, Union[List[str], bool]]:
    """
    List contents of a directory.
    
    Args:
        directory (str, optional): Directory path to list. Defaults to current directory
        
    Returns:
        Dict[str, Union[List[str], bool]]: Dictionary containing:
            - contents (List[str]): List of directory contents
            - success (bool): True if listing was successful
            - error (str): Error message if unsuccessful
    """
    return list_directory(directory)

@mcp.tool()
async def get_file_details(file_path: str) -> Dict[str, Union[Dict, bool]]:
    """
    Get information about a file (size, modification time, etc).
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        Dict[str, Union[Dict, bool]]: Dictionary containing:
            - info (Dict): File information including:
                - size (int): File size in bytes
                - modified_time (float): Last modification timestamp
                - created_time (float): Creation timestamp
                - is_directory (bool): True if path is a directory
                - is_file (bool): True if path is a file
            - success (bool): True if info retrieval was successful
            - error (str): Error message if unsuccessful
    """
    return get_file_info(file_path)

@mcp.tool()
async def create_dir(directory_path: str) -> Dict[str, bool]:
    """
    Create a new directory.
    
    Args:
        directory_path (str): Path of directory to create
        
    Returns:
        Dict[str, bool]: Dictionary containing:
            - success (bool): True if directory creation was successful
            - error (str): Error message if unsuccessful
    """
    return create_directory(directory_path)