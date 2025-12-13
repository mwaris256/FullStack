import subprocess

def list_installed_packages():
    """
    Lists all installed Python packages using pip.
    """
    try:
        # Execute the 'pip list' command
        # capture_output=True captures stdout and stderr
        # text=True decodes stdout and stderr as text
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True, check=True)
        print("Installed Python Packages:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error listing packages: {e}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: pip command not found. Ensure pip is installed and in your system's PATH.")

if __name__ == "__main__":
    list_installed_packages()