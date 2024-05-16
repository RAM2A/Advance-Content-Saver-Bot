from os import environ 

class Config:
    API_ID = environ.get("API_ID", "24665357")
    API_HASH = environ.get("API_HASH", "beb7e4b83ada668fa85f9a9b56338f1d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6561626656:AAEofDQ_-uaIk3vJmiY1xuzjPEeczUXVNt4") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQGqa00ASVBevTCWNFPMFqNRbex5AB9dtMYUBvO3Sj2e2e4xO4ay1U1q7DRI6_Wd_3B6ePgTZ2anbwN5d-yIi_0MckOrcEir20syOxj1-Mz7ZFyd6LmESh6uPSvAxNwl-SWJNH7_UIw7BZ6AknacsP3_Cne_AIxGVZU_cTmU7aIWAkpfg_XfYKKMFPCKrtx2V1-fij_FSFY9FKWDWu17mBRiUU9hCWQAVZleIS9nG1pqKLhHqhmDULGzVl5mam1ZKxhF9LidGHccCvO4eWrVOVdOS821qmQl5M0Jparn-eCAmuRVxwfSndUmb09tpt3QCjy8-JIiroWZ_BqYKhqqbvaoK3PJAAAAAAGPYiOpAQ") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://lisafeh696:ZHtN2jDPpkubuJH3@srcbot.uxq3prr.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "srcbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1717511106').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
