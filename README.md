# Project Khepri

A toolkit that enables AI models to interact with the file system, execute commands, and access web information to build projects.

## Repository Contents

- **tools.py**: Core functionality providing utilities for:
  - Command execution
  - File operations (read/write/append)
  - Web connectivity (search and content fetching)
  - Project planning management

## Available Functions

### Command Line Tools
- `run_command(command)`: Executes a shell command and returns structured output with stdout, stderr, and exit code

### File Operations
- `read_file(file_path)`: Reads and returns the contents of a file
- `write_file(file_path, content, mode)`: Writes content to a file (overwrite or append)
- `append_file(file_path, content)`: Appends content to a file
- `list_directory(directory)`: Lists contents of a directory
- `get_file_info(file_path)`: Returns file metadata (size, modification time, etc.)
- `create_directory(directory_path)`: Creates a new directory

### Web Connectivity
- `web_search(query)`: Performs a web search using Google Custom Search API
- `web_fetch(url)`: Fetches content from a specific URL

### Project Planning
- `create_project_plan(plan_content)`: Creates or updates the project action plan
- `append_to_project_plan(additional_content)`: Adds content to the existing project plan
- `read_project_plan()`: Retrieves the current project plan

### Utilities
- `get_functions_schema()`: Returns a JSON schema of all available functions

## Usage

Run the script directly to see available functions:

```
python tools.py
```

Or run a command:

```
python tools.py ls -la
```

## Requirements

- Python 3.6+
- requests library
- Environment variables for web search:
  - GOOGLE_API_KEY
  - GOOGLE_SEARCH_ENGINE_ID 