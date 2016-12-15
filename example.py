import sys
from pluralsight.licensing import LicensingAPIClient
from pluralsight.reports import ReportsAPIClient
from pprint import pprint

# get the API key and plan from the command line
api_key = sys.argv[1]
plan = sys.argv[2]

# Create a client to the licensing API
client = LicensingAPIClient(plan, api_key)

# Get all invites
invites = client.invites.get_all_invites()
pprint(invites)


# Create  a client for the reporting API
reports = ReportsAPIClient(plan, api_key)

# Download the user reports
reports.download_user_report(plan, '.')