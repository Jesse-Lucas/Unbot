from selenium import webdriver
import time
from selenium.webdriver.support.select import Select   

class Teste:
    def __init__(self):
        self.login_usuario = "180122908"
        self.login_senha = "Kalmar91"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <input id="username" name="username" class="col-12" tabindex="2" placeholder="Digite seu login" autofocus="autofocus" type="text" value="" size="25" maxlength="20" autocomplete="off">
        # <input id="password" name="password" class="col-12" tabindex="3" placeholder="Digite sua senha" type="password" value="" size="25" maxlength="64" autocomplete="off">
        # <button tabindex="4" name="submit" value="Submit" form="login-form" class="btn-login cursor-pointer opacity-1 col-5">
        #                ENTRAR <i class="fas fa-greater-than"></i>
        #            </button>
        self.driver.get('https://sig.unb.br/sigaa/portais/discente/discente.jsf')
        time.sleep(2)

        caixa_usuario = self.driver.find_element_by_id('username')
        time.sleep(1)
        caixa_usuario.click()
        caixa_usuario.send_keys(self.login_usuario)
        time.sleep(1)
        caixa_senha = self.driver.find_element_by_id('password')
        time.sleep(1)
        caixa_senha.click()
        caixa_senha.send_keys(self.login_senha)
        time.sleep(1)
        botao_enviar = self.driver.find_element_by_xpath("//button[@name='submit']")
        time.sleep(1)
        botao_enviar.click()
        time.sleep(3)
        # <td class="ThemeOfficeMenuItemText">Emitir Atestado de Matrícula</td>
        # achar_matricula = self.driver.find_element_by('Emitir Atestado de Matrícula')
        # time.sleep(2)
        # achar_matricula.click()
        # time.sleep(4)

        # <td class="ThemeOfficeMainItem" onmouseover="cmItemMouseOver (this,'ThemeOffice',1,'cmSubMenuID1','hbr',0)" onmousemMouseout="cmIteOut (this,500)" onmousedown="cmItemMouseDown (this,0)" onmouseup="cmItemMouseUp (this,0)"><span class="ThemeOfficeMainFolderLeft"><img src="/sigaa/img/icones/ensino_menu.gif"></span><span class="ThemeOfficeMainFolderText">Ensino</span><span class="ThemeOfficeMainFolderRight">&nbsp;</span></td>
        # menu_form_menu_discente_j_id_jsp_340461267_98_menu
        # achar_ensino = self.driver.find_element_by_class_name('ThemeOfficeMainItem')
        # achar_ensino.click()
        # time.sleep(2)

        achar_matricula = self.driver.find_element_by_xpath("//*[@id='menu_form_menu_discente_j_id_jsp_340461267_98_menu']/table/tbody/tr/td[1]/span[2]")
        achar_matricula.click()
        time.sleep(1)
        testao = self.driver.find_element_by_xpath("//*[@id='cmSubMenuID1']/table/tbody/tr[4]")
        testao.click()
        time.sleep(1)

bot = Teste()
bot.EnviarMensagens()

