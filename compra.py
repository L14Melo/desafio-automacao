import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def setup():
    data = []

    with open('data_set.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            item = {
                'username': row[0],
                'password': row[1],
                'firstName': row[2],
                'lastName': row[3],
                'postalCode': row[4],
            }
            data.append(item)

    return data


def logar(wait, data):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="username"]'))).send_keys(data[0]['username'])
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="password"]'))).send_keys(data[0]['password'])
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="login-button"]'))).click()


def adicionar_carrinho(wait):
    buttons = wait.until(
        ec.visibility_of_all_elements_located((By.CLASS_NAME, 'btn_inventory'))
    )
    for button in buttons:
        button.click()


def checkout(wait):
    wait.until(ec.visibility_of_element_located((By.ID, 'shopping_cart_container'))).click()
    wait.until(ec.visibility_of_element_located((By.ID, 'checkout'))).click()



def preencherEndereco(wait, data):
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="firstName"]'))).send_keys(data[0]['firstName'])
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="lastName"]'))).send_keys(data[0]['lastName'])
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="postalCode"]'))).send_keys(data[0]['postalCode'])
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="continue"]'))).click()

def valor_total(wait):

    total_element = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_element.text
    print(total)

def finalizar(wait):
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="finish"]'))).click()

    time.sleep(5)


servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
wait = WebDriverWait(driver, 20)     #Utilizei a biblioteca WebDriverWait e ExpectConditions para que o código
                                            # aguarde até que os elementos estejam disponíveis na tela.
data = setup()
logar(wait, data)
adicionar_carrinho(wait)
checkout(wait)
preencherEndereco(wait, data)
valor_total(wait)
finalizar(wait)

driver.quit()