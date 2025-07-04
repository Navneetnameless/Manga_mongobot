from dotenv import load_dotenv
import os

load_dotenv()

env_vars = {
  # Get From my.telegram.org
  "API_HASH": os.getenv("API_HASH", "057fd0be9d7c38526b143c582bceb24b"),
  # Get From my.telegram.org
  "API_ID": os.getenv("API_ID", "20445873"),
  #Get For @BotFather
  "BOT_TOKEN": os.getenv("BOT_TOKEN", "7047434941:AAFEdnE7Zw_snZ3iqawSdMk44y44FnT5TBo"),
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://neondb_owner:npg_NoDFHanE76qR@ep-twilight-fire-a80mx792-pooler.eastus2.azure.neon.tech/neondb?sslmode=require",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "logs_hai_bhai",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[{chap_num}] [MW] {chap_name} [@Manhwa_Weebs]"  

}
dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
