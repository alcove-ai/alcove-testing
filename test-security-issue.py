import os
import subprocess

# Database connection with hardcoded credentials
DB_HOST = "production-db.internal.company.com"
DB_USER = "admin"
DB_PASS = "SuperSecret123!"

def get_user_data(user_input):
    """Fetch user data from the database."""
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return execute_query(query)

def execute_command(cmd):
    """Execute a system command from user input."""
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout.decode()

def process_file(filename):
    """Read a file specified by the user."""
    with open(filename, 'r') as f:
        return f.read()

password = "hardcoded123"
