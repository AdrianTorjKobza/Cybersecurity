import re # Regular Expression module
import sys

# High-risk patterns: AWS Keys, Generic API Keys, Private Keys.
PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic Secret": r"(?i)secret(_|token|key)?\s*[:=]\s*['\"][0-9a-zA-Z]{16,}['\"]",
    "Private Key": r"-----BEGIN RSA PRIVATE KEY-----"
}

def scan_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        for name, pattern in PATTERNS.items():
            if re.search(pattern, content):
                print(f"❌ SECURITY ALERT: {name} found in {file_path}!")
                return True
            
    return False

def main():
    files = sys.argv[1:] # Capture the files names.
    found_issue = False # Assume the code is safe, until proven otherwise.

    # Loop through the files.
    for file in files:
        if scan_file(file):
            found_issue = True
    
    if found_issue:
        sys.exit(1) # Block the commit.

if __name__ == "__main__":
    main()