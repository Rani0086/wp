class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5886080930"
    sudo_users = "5886080930", "7526369190", "6961287189"
    GROUP_ID = -1002137208192
    TOKEN = "8198269280:AAF9Kz2w34rzWgw2VjHedTOLEjH3k7Xq9bo"
    mongo_url = "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/ed23556d07d33db18402d.jpg", "https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg"]
    SUPPORT_CHAT = "kill_your_HW_Group"
    UPDATE_CHAT = "kill_your_HW_Channel"
    BOT_USERNAME = "Kill_Your_HW_Bot"
    CHARA_CHANNEL_ID = "-1002489030940"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
