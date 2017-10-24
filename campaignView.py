import ZODB, ZODB.FileStorage
from campaign import Campaign

storage = ZODB.FileStorage.FileStorage('mycampaign.fs')
db = ZODB.DB(storage)
connection = db.open()
campaign_root = connection.root
print(campaign_root.campaign.party.players)
