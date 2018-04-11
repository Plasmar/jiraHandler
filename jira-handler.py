# Cameron M, Merrick

# jira-handler.py

# A script used internally for our SALT Vulnerability Management program
# Script used to ingest and parse vulnerbility reports from 3rd parties
# provided as csv files, and then create tickets and assign persons responsible
# for remediation of each vulnerability.

import os
from openpyxl import Workbook               # For working w/ MS Excel files
import datetime
from datetime import date as dt


class VulnObject:
    
    def __init__(self, title, severity, source, qid, vendor):

                                            # Initialize from the parser
        self.title = title                  # with the fields passed to it
        self.severity = severity
        self.source = source
        self.dateReported = dt.today()
        self.qid = qid
        self.vendor = vendor
    
    def printTitle(self):                   # Test by printing the title line
        print(str(self.title))
        return

def testModule():

                                            # create dummy data for test
    title = "Apache HTTP Server Prior to 2.4.30 Multiple Vulnerabilities"
    severity = 5
    source = "Qualys Daily Vulnerability Report"
    qid = 390114
    vendor = "Apache 2.4.30"
    vuln1 = VulnObject(title, severity, source, qid, vendor)
    vuln1.printTitle()                      # Print test line
    return vuln1                            # Return the whole object

# Will return the creation or modified date of the file "Latest_vulnerabilities.csv"
# to check if new tickets should be created or not for the given file
def creation_date(pathToFile):
    stat = os.stat(pathToFile)
    try:
        return stat.st_birthtime            # Check creation date
    except AttributeError:
        return stat.st_mtime                # If not found, go with modified dt
def main():

    today = dt.today()                      # # Create timestamp 

    # Move to the dir where we want to save persisting files
    os.chdir('/Users/cmerrick/code/git/Environments/jira-handler/')
    distro_file_unixts = creation_date('/Users/cmerrick/code/git/Environments/jira-handler/Latest_vulnerabilities.csv')
    distro_file_date = dt.fromtimestamp(distro_file_unixts)
# *****************************************************************#
    if (os.path.isfile((str(today) + ".xls")) or distro_file_date != today):
        os.sys.exit(2)
    wb = Workbook()                         # Create workbook object
    ws = wb.active
    ws.title = "Remediation Assignments"    # Rename the worksheet
    wb.save(str(today) + ".xls")            # Rename the workbook

    vuln1 = testModule()                    # # Run initial tests
    return


if __name__ == '__main__':
    main()
