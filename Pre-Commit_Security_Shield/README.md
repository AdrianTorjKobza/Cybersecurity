# Pre-Commit_Security_Shield

The tool prevents hardcoded secrets (e.g. AWS Keys, API Keys) and insecure code patterns from reaching the remote repository.

## Workflow

1. **Developer triggers `git commit`.**
2. **Tool Performs:**
   - **Key Scanning:** Scans for AWS Keys, API Keys using regex.
   - **SAST (Static Analysis):** Runs `Bandit` to detect SQL injection, unsafe imports, and hardcoded passwords in Python.
3. **Pass/Fail:** If security flaws are found, the commit is blocked, and the developer is notified.