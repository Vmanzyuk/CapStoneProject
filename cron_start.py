import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ActualTokenList.settings")
django.setup()

from TokensDB.cron_scripts.cmc_update_usd_price import cmc_update_usd_price

cmc_update_usd_price()
