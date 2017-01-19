# This script will find an invitation for a user and show you the invite link

from pluralsight.licensing import LicensingAPIClient
import sys

invite_email = sys.argv[1]
plan = sys.argv[2]
api_key = sys.argv[3]

client = LicensingAPIClient(plan, api_key)

invites = client.invites.get_invites(email=invite_email)

print("Found {0} invites".format(len(invites)))

for invite in invites:
    print("Link - " + invite.generate_url(plan))
