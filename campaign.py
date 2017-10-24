import ZODB, ZODB.FileStorage, transaction, persistent
from campaignObject import Campaign


storage = ZODB.FileStorage.FileStorage('mycampaign.fs')
db = ZODB.DB(storage)
connection = db.open()
campaign = connection.root

#campaign.campaignObject = Campaign()
campaign.campaignObject.party.addPlayer("Gab")
campaign.campaignObject._p_changed = True
transaction.commit()
