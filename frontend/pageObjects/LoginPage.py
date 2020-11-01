class LoginPage():
    textbox_username_id = 'user'
    textbox_password_id = 'password'
    button_login = 'login'
    button_submit = 'login-submit'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.button_login).click()

    def click_submit(self):
        self.driver.find_element_by_id(self.button_submit).click()
