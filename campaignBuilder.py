import ZODB, ZODB.FileStorage, transaction, persistent
from campaign import Campaign


storage = ZODB.FileStorage.FileStorage('mycampaign.fs')
db = ZODB.DB(storage)
connection = db.open()
campaign_root = connection.root

campaign_root.campaign = Campaign()
campaign_root.campaign.newParty()
campaign_root.campaign.addPlayer("Jeremie")
transaction.commit()

