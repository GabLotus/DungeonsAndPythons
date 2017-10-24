import ZODB, ZODB.FileStorage
from campaignObject import Campaign

storage = ZODB.FileStorage.FileStorage('mycampaign.fs')
db = ZODB.DB(storage)
connection = db.open()
campaign = connection.root
print(campaign.name)
print(campaign.campaignObject.test_array)