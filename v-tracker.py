from requests import get
import telegram_send


URL = "http://beta.mcdstate.info/"
R = get(URL)
if R.status_code != 200:
    telegram_send.send(messages=["FATAL: beta.mcdstate.info is down"])

URL = "https://tracker-vaults.makerdao.network/"
R = get(URL)
if R.status_code != 200:
    telegram_send.send(messages=["FATAL: tracker-vaults.makerdao.network is down"]) 


# */5 * * * * /home/ubuntu/airflow-scheduler-monitor/env/bin/python monitor.py
# /home/ubuntu/airflow-scheduler-monitor/env/bin/python /home/ubuntu/trackers-monitor/v-tracker.py
