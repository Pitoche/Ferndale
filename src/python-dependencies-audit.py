import subprocess
from datetime import datetime
import os
import sqlite3
import re

# Define the folder where the report will be saved
reports_folder = "/home/angel/ADL-TOOL/reports"

# Ensure the reports folder exists
os.makedirs(reports_folder, exist_ok=True)

# Create a timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_filename = f"pip-audit-{timestamp}.log"
report_filepath = os.path.join(reports_folder, report_filename)

# Run pip-audit and save the output to the file
try:
    with open(report_filepath, "w") as report_file:
        result = subprocess.run(
            ["pip-audit"],
            stdout=report_file,
            stderr=subprocess.STDOUT
        )
        if result.returncode == 0:
            print(f"No vulnerabilities found. Report saved to {report_filepath}")
        else:
            print(f"Vulnerabilities found. Report saved to {report_filepath}")
    
    # Now parse the report and populate the vulnerabilities table
    with open(report_filepath, "r") as report_file:
        lines = report_file.readlines()
    
    # Establish a database connection
    conn = sqlite3.connect("/home/angel/ADL-TOOL/ADL-TOOL-DB.db")
    cursor = conn.cursor()
    
    # Parse the report
    vulnerabilities = []
    for line in lines:
        # Define regex patterns to capture each column
        # Example line: 'Name         Version    ID                  Fix Versions'
        match = re.match(r"(?P<name>\S+)\s+(?P<version>\S+)\s+(?P<vulnerability_id>\S+)\s+(?P<fix_version>[\S\s]+)(?:\s+(?P<skip_reason>.*))?", line)
        
        if match:
            vulnerability = {
                "name": match.group("name"),
                "version": match.group("version"),
                "vulnerability_id": match.group("vulnerability_id"),
                "fix_version": match.group("fix_version").strip(),
                "skip_reason": match.group("skip_reason") if match.group("skip_reason") else None
            }
            vulnerabilities.append(vulnerability)
    
    # Insert the vulnerabilities into the database
    for vuln in vulnerabilities:
        cursor.execute('''
            INSERT INTO vulnerabilities (name, version, vulnerability_id, fix_version, skip_reason, type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (vuln["name"], vuln["version"], vuln["vulnerability_id"], vuln["fix_version"], vuln["skip_reason"], "PIP-AUDIT"))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Vulnerabilities have been saved to the database. Report saved to {report_filepath}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
