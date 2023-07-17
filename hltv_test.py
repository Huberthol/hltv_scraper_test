import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time


browser = uc.Chrome()
browser.get('https://www.hltv.org/matches/2363941/illuminar-vs-sangal-cct-central-europe-series-6')
time.sleep(3)
#accept cookies
browser.find_element(By.CSS_SELECTOR, '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
time.sleep(3)
#previous match on the right
browser.find_element(By.CSS_SELECTOR, 'body > div.bgPadding > div.widthControl > div:nth-child(2) > div.contentCol > div.match-page > div.past-matches.spoiler > div:nth-child(3) > div:nth-child(2) > div.past-matches-scroll-area > table > tbody > tr:nth-child(1) > td.past-matches-score > a').click()
time.sleep(3)
#print table match data of the individal plays of the players
tabela = browser.find_element(By.CSS_SELECTOR, '#match-stats').text
print(tabela)
