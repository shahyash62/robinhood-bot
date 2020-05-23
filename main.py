import robin_stocks as r
import pandas as pd
import config

login = r.login(config.username, config.password)
print(login)
