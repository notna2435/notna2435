from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import os.path
from selenium.webdriver.common.keys import Keys
import time
import re

SAMPLE_LIST = ['AgenT', 'Acclinate', 'AmacaThera', 'Atro Medical', 'biotx.ai', 'Grapheal', 'MabSwitch, Inc',
               'siRNAgen Therapeutics', 'Vaxess Technologies']

# Set up the web driver
service = Service('/Users/yue/notna2435/chromedriver')
driver = webdriver.Chrome(service=service)
url = 'https://jnjinnovation.com/innovation-challenges/awardees'
driver.get(url)
time.sleep(5)

# select element with class tooltiptext in the current html page
company_elements = driver.find_elements(By.CLASS_NAME, 'tooltiptext')
element_list = []
name_and_award = [element_list.append(element.text.splitlines()) for element in company_elements]
sample_elements = []
for x in element_list:
    for company in SAMPLE_LIST:
        if company == x[0]:
            sample_elements.append(x)
# print(sample_elements)

time.sleep(5)
sample_link_list = []
wait = WebDriverWait(driver, 5)
company_images = driver.find_elements(By.CLASS_NAME, 'sponsorsbox')

# modal = driver.find_elements(By.ID, 'onetrust-accept-btn-handler')

# handle cookie policy modal
overlay_close_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
print('overlay_close_button', overlay_close_button)
if overlay_close_button:
    driver.execute_script("arguments[0].click();", overlay_close_button)

# # Wait for the overlay to disappear
wait = WebDriverWait(driver, 10)
overlay = wait.until(EC.invisibility_of_element_located((By.ID, 'ot-sdk-container')))

try:
    leadingModal = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'leadinModal-close')))

    print('leadingModal', leadingModal)
    if leadingModal:
        driver.execute_script("arguments[0].click();", leadingModal)
except Exception as e:
    print('errroor', e)
finally:
    for c in range(0, len(company_images)):
        print('sample_link_list length', len(sample_link_list))
        print('SAMPLE_LIST length', len(SAMPLE_LIST))
        if len(sample_link_list) >= len(SAMPLE_LIST):
            break
        elif company_images[c].is_displayed():
            print('company_images90', company_images[c])
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView(true);", company_images[c])
            # time.sleep(2)
            # company_images[c].click()
            driver.execute_script("arguments[0].click();", company_images[c])
            time.sleep(0.25)
            heading = driver.find_element(By.CLASS_NAME, 'descriptioncontent').text.splitlines()
            print('heading', heading)
            if heading[0] in SAMPLE_LIST:
                print('length', len(sample_link_list))
                company_link = driver.find_element(By.LINK_TEXT, 'Learn more')
                print('company_link', company_link)
                print(company_link.get_attribute('href'))
                sample_link_list.append(company_link.get_attribute('href'))
            x_button = driver.find_element(By.CLASS_NAME, 'xbutton')
            x_button.click()
            driver.execute_script('arguments[0].scrollIntoView();', company_images[c])
        

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
}

email_list = []
phone_list = []
address_list = []

# SAMPLE_LIST = ['AgenT', 'Acclinate', 'AmacaThera', 'Atro Medical', 'biotx.ai', 'Grapheal', 'MabSwitch, Inc',
#                'siRNAgen Therapeutics', 'Vaxess Technologies']
# sample_link_list = ['https://www.vaxess.com/', 'https://www.agent-biotech.com/', 'https://www.acclinate.com/', 'https://www.amacathera.ca/',
# 'https://dev.atromedical.com/', 'https://www.biotx.ai/', 'https://www.grapheal.com/', 'https://mabswitch.com/', 'https://www.sirnagen.com/', 
# 'https://www.sirnagen.com/']

# Send an HTTP GET request to the company website
# response = requests.get(sample_link_list[1])

# # Extract the HTML content from the response
# html_content = response.text
# print('html_content', html_content)
# # Define regex patterns for contact information
# company_name_pattern = r'<h1>(.*?)</h1>'
# email_pattern = r'[\w\.-]+@[\w\.-]+'
# phone_pattern = r'\+?\d{2} \d{1,2} \d{2} \d{2} \d{2} \d{2}| \d{3} \d{3}-\d{4}'
# address_pattern = r'STATION F, 14 rue Eug[^\n]+\n\d{5} [A-Za-z, ]+'

# # Extract contact information using regex patterns
# # company_name = re.search(company_name_pattern, html_content).group(1)
# email_list = list(dict.fromkeys(re.findall(email_pattern, html_content)))
# phone_list = list(dict.fromkeys(re.findall(phone_pattern, html_content)))
# address_list = list(dict.fromkeys(re.findall(address_pattern, html_content)))

# # Print the extracted contact information
# # print("Company Name:", company_name)
# print("Email:", email_list)
# print("Phone:", phone_list)
# print("Address:", address_list)

try:

    #Vaxess Contact Info
    driver.get(sample_link_list[0])
    time.sleep(2)
    vaxess_address = driver.find_element(By.XPATH, '//*[@id="block-13d4d317044cfd51f303"]/div/div/p[1]').text
    vaxess_email = driver.find_element(By.XPATH, '//*[@id="block-13d4d317044cfd51f303"]/div/div/p[4]').text
    vaxess_phone = 'None'

    email_list.append(vaxess_email)
    phone_list.append(vaxess_phone)
    address_list.append(vaxess_address)

    print("9 Vaxess Contact Info Email:", email_list)
    print("9 Vaxess Contact Info Phone:", phone_list)
    print("9 Vaxess Contact Info Address:", address_list)
    # AgenT Contact Info

    driver.get(sample_link_list[1])
    time.sleep(5)
    agent_contact = driver.find_element(By.LINK_TEXT, 'Contact').get_attribute('href')
    print('agent_contact', agent_contact)

    response_1 = requests.get(
        agent_contact, headers=header)

    agent_data = response_1.text
    soup = BeautifulSoup(agent_data, 'html.parser')

    email = soup.find('a', class_='lead')
    agent_email = email.getText()

    address_and_phone = soup.find_all('span', class_='lead')
    address_and_phone_text = [text.getText().strip() for text in address_and_phone]

    modified_list = []
    for element in address_and_phone_text:
        modified_element = element.replace('\n', ' ').strip()
        modified_element = ' '.join(modified_element.split())
        modified_list.append(modified_element)

    agent_phone = modified_list[1]
    agent_address = modified_list[0]

    email_list.append(agent_email)
    phone_list.append(agent_phone)
    address_list.append(agent_address)

    print("1 AgenT Contact Info Email:", email_list)
    print("1 AgenT Contact Info Phone:", phone_list)
    print("1 AgenT Contact Info Address:", address_list)

    # Acclinate Contact Info
    driver.get(sample_link_list[2])
    time.sleep(2)
    acclinate_contact = driver.find_element(By.LINK_TEXT, 'Contact').get_attribute('href')

    response_2 = requests.get(
        acclinate_contact, headers=header)

    data = response_2.text
    soup = BeautifulSoup(data, 'html.parser')

    acclinate_email_phone = str(soup.find('p', class_='paragraph-49')).replace('<br/>', '\n').splitlines()
    acclinate_phone = acclinate_email_phone[2]
    acclinate_email = acclinate_email_phone[3]
    acclinate_address_element = str(soup.find('p', class_='paragraph-48')).replace('<br/>', '\n').splitlines()
    acclinate_address = acclinate_address_element[4].replace('</strong>', '') + ', ' + acclinate_address_element[5].replace('</p>', '')

    email_list.append(acclinate_email)
    phone_list.append(acclinate_phone)
    address_list.append(acclinate_address)

    print("2 Acclinate Contact Info Email:", email_list)
    print("2 Acclinate Contact Info Phone:", phone_list)
    print("2 Acclinate Contact Info Address:", address_list)

    #AmacaThera Contact Info
    response_3 = requests.get(
        sample_link_list[3], headers=header)

    data = response_3.text
    soup = BeautifulSoup(data, 'html.parser')

    amacathera_contact_info = soup.find('div', class_='contact').text.splitlines()
    amacathera_phone = amacathera_contact_info[1]
    amacathera_address = amacathera_contact_info[2] + ' ' + amacathera_contact_info[3].replace('\xa0', ' ') + ' ' + amacathera_contact_info[4].replace('inf[email\xa0protected]', '')
    amacathera_email = 'info@amacathera.ca'

    email_list.append(amacathera_email)
    phone_list.append(amacathera_phone)
    address_list.append(amacathera_address)

    print("3 AmacaThera Contact Info Email:", email_list)
    print("3 AmacaThera Contact Info Phone:", phone_list)
    print("3 AmacaThera Contact Info Address:", address_list)

    # Atro Medical Contact Info
    driver.get(sample_link_list[4])
    time.sleep(2)
    atro_medical_contact = driver.find_element(By.LINK_TEXT, 'Contact').get_attribute('href')

    response_4 = requests.get(
        atro_medical_contact, headers=header)

    data = response_4.text
    soup = BeautifulSoup(data, 'html.parser')

    atro_medical_info = soup.find('p', class_='sc-jSMfEi inoWfC')
    atro_medical_email = str(atro_medical_info.find('a')).split('"')[1].replace('mailto:', '')
    split_atro_medical_info = str(atro_medical_info).replace('<br/>', '\n').splitlines()
    atro_medical_address = split_atro_medical_info[1].replace('<!-- -->', ', ') + split_atro_medical_info[2].replace('<!-- -->', '')
    atro_medical_phone = 'None'

    email_list.append(atro_medical_email)
    phone_list.append(atro_medical_phone)
    address_list.append(atro_medical_address)

    print("4 Atro Medical Contact Info Email:", email_list)
    print("4 Atro Medical Contact Info Phone:", phone_list)
    print("4 Atro Medical Contact Info Address:", address_list)

    #biotx.ai Contact Info
    response_5 = requests.get(
        sample_link_list[5], headers=header)

    data = response_5.text
    soup = BeautifulSoup(data, 'html.parser')

    biotx_email_phone = str(soup.find('div', class_='undefined').find_all('li', class_='nav-item')).replace('<!-- -->', '\n').splitlines()
    biotx_email = biotx_email_phone[7].strip()
    biotx_phone = biotx_email_phone[3].strip()
    biotx_address_element = str(soup.find('div', class_='undefined').find_all('p')).replace('<p>', '\n').splitlines()
    biotx_address = biotx_address_element[3].replace('</p>]', '')

    email_list.append(biotx_email)
    phone_list.append(biotx_phone)
    address_list.append(biotx_address)

    print("5 biotx.ai Contact Info Email:", email_list)
    print("5 biotx.ai Contact Info Phone:", phone_list)
    print("5 biotx.ai Contact Info Address:", address_list)

    # Grapheal Contact Info
    driver.get(sample_link_list[6])
    time.sleep(2)
    grapheal_contact = driver.find_element(By.XPATH, '//*[@id="comp-igauz7ee6"]/a').get_attribute('href')

    driver.get(grapheal_contact)
    grapheal_address_row1 = driver.find_element(By.XPATH, '//*[@id="comp-kvs16ime"]/p[1]/span/span/span/span').text
    grapheal_address_row2 = driver.find_element(By.XPATH, '//*[@id="comp-kvs16ime"]/p[2]/span/span/span/span').text
    grapheal_address_row3 = driver.find_element(By.XPATH, '//*[@id="comp-kvs16ime"]/p[3]/span/span/span/span').text
    grapheal_address = grapheal_address_row1 + ' ' + grapheal_address_row2 + ', ' + grapheal_address_row3.strip()
    grapheal_phone_1 = driver.find_element(By.XPATH, '//*[@id="comp-kvs16ime"]/p[6]/span/span/span/span').text
    grapheal_phone_2 = driver.find_element(By.XPATH, '//*[@id="comp-kvs16ime"]/p[7]/span/span/span/span/span').text
    grapheal_phone = grapheal_phone_1.replace('Tel: ', '') + ', ' + grapheal_phone_2.replace('Tel: ', '')

    response_6 = requests.get(
        grapheal_contact, headers=header)

    data = response_6.text
    soup = BeautifulSoup(data, 'html.parser')

    grapheal_contact_info = soup.find('div', id='comp-kvs16ime')
    grapheal_email = grapheal_contact_info.find('a').get_text()

    email_list.append(grapheal_email)
    phone_list.append(grapheal_phone)
    address_list.append(grapheal_address)

    print("6 Grapheal Contact Info:", email_list)
    print("6 Grapheal Contact Info:", phone_list)
    print("6 Grapheal Contact Info:", address_list)

    # MabSwitch Contact Info
    driver.get(sample_link_list[7])
    time.sleep(2)
    mabswitch_email_element = driver.find_element(By.XPATH, '//*[@id="contact"]/div/div/div[1]/div/div[2]/div[2]').text
    mabswitch_email = mabswitch_email_element.replace(' (at) ', '@').replace('Email Us\n', '')
    mabswitch_phone = 'None'
    mabswitch_address = 'None'

    email_list.append(mabswitch_email)
    phone_list.append(mabswitch_phone)
    address_list.append(mabswitch_address)

    print("7 MabSwitch Contact Info Email:", email_list)
    print("7 MabSwitch Contact Info Phone:", phone_list)
    print("7 MabSwitch Contact Info Address:", address_list)

    # siRNAgen Contact Info
    response_8 = requests.get(
        sample_link_list[8], headers=header)

    data = response_8.text
    soup = BeautifulSoup(data, 'html.parser')

    sirnagen_email = str(soup.find_all('a', class_='wixui-rich-text__text')[1]['href']).replace('mailto:', '')
    sirnagen_phone = 'None'
    sirnagen_address = 'None'

    email_list.append(sirnagen_email)
    phone_list.append(sirnagen_phone)
    address_list.append(sirnagen_address)

    print("8 siRNAgen Contact Info Email:", email_list)
    print("8 siRNAgen Contact Info Phone:", phone_list)
    print("8 siRNAgen Contact Info Address:", address_list)

except Exception as e:
    print('error', e)
finally:
    driver.quit()  # DRIVER QUITS RIGHT HERE

#                             -------PUT DATA IN DATABASE-------

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company-contacts.db'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'company-contacts.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'sample_python'
db = SQLAlchemy(app)


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(250), nullable=False, unique=True)
    award = db.Column(db.String(250), nullable=False)
    link = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250))
    phone_number = db.Column(db.String(250))
    address = db.Column(db.String(250))


with app.app_context():
    db.create_all()

    print('weqweqwe', sample_elements)
    print('weqweqwe len', len(sample_elements))

    for i in range(0, len(sample_elements)):
        if len(sample_elements[i]) == 1:
            new_item = Sample(company_name=sample_elements[i][0], award="None", link=sample_link_list[i],
                              email=email_list[i], phone_number=phone_list[i], address=address_list[i])
        else:
            new_item = Sample(company_name=sample_elements[i][0], award=sample_elements[i][1].replace("Awardee of ", ""),
                              link=sample_link_list[i], email=email_list[i], phone_number=phone_list[i], address=address_list[i])
        db.session.add(new_item)

    # new_item = Sample(company_name=get_random_string(2), award=get_random_string(4), link=get_random_string(5),
                            #    email=get_random_string(6), phone_number=get_random_string(5), address=get_random_string(6))
    
    db.session.add(new_item)

    db.session.commit()
time.sleep(2)

    