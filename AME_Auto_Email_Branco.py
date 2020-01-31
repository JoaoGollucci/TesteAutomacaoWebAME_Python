from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint

testid = str(randint(1, 9999))

log = open("log_teste_"+testid+".txt", "w")

log.write("Iniciando Teste \n")
log.write("----- \n")

#Abrir Navegador Chrome (fullscreen)
browser = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
browser.implicitly_wait(20)
browser.maximize_window()

log.write("Navegador aberto \n")
log.write("----- \n")

#Acessar URL
browser.get("http://automationpractice.com/index.php")

log.write("Site Acessado \n")
log.write("----- \n")

browser.find_element_by_xpath("//a[@class='login']").click()

log.write("Iniciando Login \n")
log.write("----- \n")

browser.find_element_by_xpath("//button[@id='SubmitLogin']").click()

log.write("E-mail Não Preenchido \n")
log.write("----- \n")
log.write("Logando \n")
log.write("----- \n")

#Validando Mensagem de Erro (email inválido)
validar_texto = browser.find_element_by_xpath("//div[@class='alert alert-danger']/ol/li").text
assert validar_texto == "An email address required."

log.write("Mensagem de Erro Apresentada \n")
log.write("----- \n")

browser.quit()

log.write("Navegador fechado \n")
log.write("----- \n")

log.write("Teste Executado com Sucesso ! \n")
log.close()
