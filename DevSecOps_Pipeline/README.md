# DevSecOps Pipeline

CI/CD pipeline template to enforce security at every stage of the software development lifecycle. It integrates SCA, SAST, Container Scanning, and DAST into a single automated workflow.

## Pipeline Stages
1. **SCA (Trivy):** Analyzes `requirements.txt` for publicly known vulnerabilities (CVEs).
2. **SAST (Bandit):** Inspects Python source code for logic flaws like SQL Injection.
3. **Container Security:** Scans the Docker base image for OS-level threats.
4. **DAST (OWASP ZAP):** Performs black-box testing against the running application.

## How to Use
1. Fork this repository.
2. Ensure **GitHub Actions** are enabled in your repository settings.
3. Push any change to the `app/` folder.
4. Watch the **Actions** tab to see the security gates in action.
