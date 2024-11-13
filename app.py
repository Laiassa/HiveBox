# app.py

import sys

def print_version():
    version = "v0.0.1"  # Define the app version using Semantic Versioning
    print(f"App Version: {version}")
    sys.exit()  # Exit the application after printing the version

if __name__ == "__main__":
    print_version()
