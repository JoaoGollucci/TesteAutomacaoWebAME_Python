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

#Acessar
browser.get("http://automationpractice.com/index.php")

log.write("Site Acessado \n")
log.write("----- \n")

#Criar Conta
email = "teste"+testid+"@ame.com.br"
browser.find_element_by_xpath("//a[@class='login']").click()
browser.find_element_by_xpath("//input[@id='email_create']").send_keys(email)
browser.find_element_by_xpath("//button[@id='SubmitCreate']").click()

log.write("Iniciando Criação de Conta \n")
log.write("----- \n")

browser.find_element_by_xpath("//input[@id='id_gender1']").click()

browser.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("Teste")
browser.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("Teste")

browser.find_element_by_xpath("//input[@id='passwd']").send_keys("teste123")

dia = Select(browser.find_element_by_xpath("//select[@id='days']"))
dia.select_by_value("11")

mes = Select(browser.find_element_by_xpath("//select[@id='months']"))
mes.select_by_value("6")

ano = Select(browser.find_element_by_xpath("//select[@id='years']"))
ano.select_by_value("1995")


browser.find_element_by_xpath("//input[@id='firstname']").send_keys("Teste")
browser.find_element_by_xpath("//input[@id='lastname']").send_keys("Teste")
browser.find_element_by_xpath("//input[@id='address1']").send_keys("Rua Teste 42")
browser.find_element_by_xpath("//input[@id='city']").send_keys("Cidade Teste")

estado = Select(browser.find_element_by_xpath("//select[@id='id_state']"))
estado.select_by_value("1")

browser.find_element_by_xpath("//input[@id='postcode']").send_keys("12345")

pais = Select(browser.find_element_by_xpath("//select[@id='id_state']"))
pais.select_by_value("1")

browser.find_element_by_xpath("//input[@id='phone_mobile']").send_keys("999999999")

browser.find_element_by_xpath("//input[@id='alias']").send_keys("Teste Casa")

browser.find_element_by_xpath("//button[@id='submitAccount']").click()

log.write("Finalizando Conta \n")
log.write("----- \n")

#Validando que a página "MY ACCOUNT" foi acessada, validando a criação da conta
validar_texto = browser.find_element_by_xpath("//h1").text
assert validar_texto == "MY ACCOUNT"

log.write("Conta Criada com Sucesso \n")
log.write("Email Utilizado: "+email+"\n")
log.write("----- \n")

browser.quit()

log.write("Navegador fechado \n")
log.write("----- \n")

log.write("Teste Executado com Sucesso ! \n")
log.close()

