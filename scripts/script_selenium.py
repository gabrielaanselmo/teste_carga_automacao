from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuração do Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar em modo headless (sem abrir o navegador)
chrome_service = Service(executable_path='./drivers/chromedriver')  # Caminho para o WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# URL do login
login_url = "https://the-internet.herokuapp.com/login"

# Acessar a página de login
driver.get(login_url)

# Inserir nome de usuário
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")  # Nome de usuário correto

# Inserir senha
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")  # Senha correta

# Submeter o formulário
password_field.send_keys(Keys.RETURN)

# Aguardar a página carregar e verificar o resultado
time.sleep(3)
success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text

if "You logged into a secure area!" in success_message:
    print("Login bem-sucedido!")
else:
    print("Falha no login.")

# Fechar o navegador
driver.quit()