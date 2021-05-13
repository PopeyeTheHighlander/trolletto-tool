import undetected_chromedriver.v2 as uc
driver = uc.Chrome()

with driver:
    # driver.get('https://yaresponsive.flarum.cloud/')
    driver.get('https://domandina.it')
logo = color.HEADER + '''

████████╗██████╗░░█████╗░██╗░░░░░██╗░░░░░███████╗████████╗████████╗░█████╗░  
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗  
░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░░░░█████╗░░░░░██║░░░░░░██║░░░██║░░██║  
░░░██║░░░██╔══██╗██║░░██║██║░░░░░██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██║░░██║  
░░░██║░░░██║░░██║╚█████╔╝███████╗███████╗███████╗░░░██║░░░░░░██║░░░╚█████╔╝  
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░  

████████╗░█████╗░░█████╗░██╗░░░░░    ██████╗░██╗░░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░    ██╔══██╗╚██╗░██╔╝
░░░██║░░░██║░░██║██║░░██║██║░░░░░    ██████╦╝░╚████╔╝░
░░░██║░░░██║░░██║██║░░██║██║░░░░░    ██╔══██╗░░╚██╔╝░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗    ██████╦╝░░░██║░░░
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝    ╚═════╝░░░░╚═╝░░░

██████╗░░█████╗░██████╗░███████╗██╗░░░██╗███████╗██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗░██╔╝██╔════╝██║
██████╔╝██║░░██║██████╔╝█████╗░░░╚████╔╝░█████╗░░██║
██╔═══╝░██║░░██║██╔═══╝░██╔══╝░░░░╚██╔╝░░██╔══╝░░╚═╝
██║░░░░░╚█████╔╝██║░░░░░███████╗░░░██║░░░███████╗██╗
╚═╝░░░░░░╚════╝░╚═╝░░░░░╚══════╝░░░╚═╝░░░╚══════╝╚═╝
                                        Author: @POPEYE EL POPE
                                        Version: 1.0
####################################### DISCLAIMER ########################################
| Trolletto tool is a tool that allows you to use to bot some no sense accounts to the    |
| DUCE's site. . Please use this tool responsibly.                                        |
| I am NOT responsible for any damages caused or any crimes committed by using this tool. |
###########################################################################################

'''
print(logo)

x=0
while x < 1:
    import time
    time.sleep(4)
    from random_username.generate import generate_username
    driver.find_element_by_class_name('item-signUp')
    elem = driver.find_element_by_class_name('item-signUp').click()
    time.sleep(1) #il programma aspetta che si carica la pagina
    driver.find_element_by_name('username')
    userName = driver.find_element_by_name('username')
    name=generate_username(1) #richiamare l'elemento con name[0] per avere la stringa
    userName.send_keys( str(name[0])) #da qui con send-keys il bot inizia a digitare
    driver.find_element_by_name('email')
    mailField =  driver.find_element_by_name('email')
    mailField.click()

    mailField.send_keys(f"{name[0]}@ADMINDIMERDASEIPEDOFI.LO")
    driver.find_element_by_name('password')
    passWord = driver.find_element_by_name('password')
    passWord.click()
    passWord.send_keys('arandomshittypasword')
    #driver.find_element_by_xpath('//*[@id="modal"]/div/div/div/form/div[2]/div[2]/div[5]/button')
    register = driver.find_element_by_xpath('//*[@id="modal"]/div/div/div/form/div[2]/div[2]/div[5]/button') #div registrati di domandina
    #register = driver.find_element_by_xpath('//*[@id="modal"]/div/div/div/form/div[2]/div[2]/div[4]/button') #div free flarum
    register.click()
    time.sleep(3)
    prifileOut = driver.find_element_by_xpath('//*[@id="header-secondary"]/ul/li[3]/div/button/span[2]')
    prifileOut.click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="header-secondary"]/ul/li[3]/div/ul/li[5]') #li logout
    eXXit = driver.find_element_by_xpath('//*[@id="header-secondary"]/ul/li[3]/div/ul/li[5]')
    eXXit.click()

    continue

    #SOLO A SCOPO ILLUSTRATIVO EDUCATIVO E BLA BLA BLA!

