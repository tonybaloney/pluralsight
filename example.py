import sys
from pluralsight.licensing import LicensingAPIClient
from pprint import pprint

api_key = sys.argv[1]
plan = sys.argv[2]

client = LicensingAPIClient(plan, api_key)

invites = client.invites.get_all_invites()
pprint(invites)
