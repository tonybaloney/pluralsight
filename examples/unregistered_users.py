# This script will get all the outstanding invitations and send them an email
# via your Exchange Web Access API.
# pip install exchangelib
# Tested on Python 3.5

from pluralsight.licensing import LicensingAPIClient

from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox
from exchangelib.folders import HTMLBody

plan = 'your-plan-name'
api_key = 'your-license-api-key'
email = 'youremail.com'
me = "Your name <{0}>".format(email)

EXCHANGE_PASSWORD = 'password 123'

# Username in WINDOMAIN\username format. Office365 wants usernames in PrimarySMTPAddress
# ('myusername@example.com') format. UPN format is also supported.
#
# By default, fault-tolerant error handling is used. This means that calls may block for a long time
# if the server is unavailable. If you need immediate failures, add 'is_service_account=False' to
# Credentials.
credentials = Credentials(username=email, password=EXCHANGE_PASSWORD)

account = Account(primary_smtp_address=email, credentials=credentials,
                  autodiscover=True)

def generate_email(invite):
    # Create message container - the correct MIME type is multipart/alternative.
    subject = "Please register for your DevOps, Developer and Automation training portal access"

    # Customize this to your own message. 
    html = """\
    <html>
      <body>
        <p>Hi,<br><br>
           Happy New Year. You should have received emails from me regarding access to pluralsight.com, invitations are limited
           to a small group of individuals, of which you are one. Invitations will expire/be reallocated for any users that
           have not accepted their invitations by the deadline. <br><br>
           This is your unique registration link - <a href="{0}">{0}</a>.
           <br><br>
           Please register this week, <u>do not forward this email</u>. Registration links are unique.<br><br>
           Regards,<br>
           
        </p>
      </body>
    </html>
    """.format(invite.generate_url(plan))

    return Message(
        account=account,
        folder=account.sent,
        subject=subject,
        body=HTMLBody(html),
        to_recipients=[Mailbox(email_address=invite.email)]
    )

client = LicensingAPIClient(plan, api_key)

invites = client.invites.get_all_invites()

print("Fetched {0} invites".format(len(invites)))

for invite in invites:
    msg = generate_email(invite)

    try:
        msg.send_and_save()
        print("Sent invite reminder to {0}".format(invite.email))
    except error:
        print(error)
        print("Failed to send invite reminder to {0}".format(invite.email))
