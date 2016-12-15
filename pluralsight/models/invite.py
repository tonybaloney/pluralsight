class Invite(object):
    def __init__(self,
                 id,
                 email,
                 team_id,
                 note,
                 send_date,
                 expires_on):
        self.id = id
        self.email = email
        self.team_id = team_id
        self.note = note
        self.send_date = send_date
        self.expires_on = expires_on
        