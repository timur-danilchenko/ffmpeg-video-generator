from selenium.webdriver.common.by import By

from .exceptions import CannotSignInError
from .functions import get_element, get_elements, get_element_clickable, rsleep, send_keys, xpath_text_lower


class YouTubeBot:
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password
        self.__log_in: bool

        self.errors = []

    def get_visibility(self, visibility):
        match visibility:
            case (True, False, False):
                visibility = "PRIVATE"
            case (False, True, False):
                visibility = "UNLISTED"
            case (False, False, True):
                visibility = "PUBLIC"
            case _:
                visibility = "PRIVATE"

        return visibility

    def get_start_up_url(self):
        self.driver.get("https://www.google.com/")

    @property
    def log_in(self):
        self.driver.get("https://myaccount.google.com/")
        check_log_in = get_element(self.driver, (By.XPATH, f".//*[text()='{self.email}']"), 5)
        return bool(check_log_in)

    def click_next_btn(self):
        pass

    def click_done_btn(self):
        pass

    def click_dismiss_btn(self):
        pass

    def check_for_errors(self) -> bool:
        for error in self.errors:
            error_element = get_element(self.driver, (By.XPATH, f".//div[{xpath_text_lower(error)}]"))
            if error_element:
                return True
        return False

    def upload_video(self, video, title: str, description="", visibility=""):
        def next_btn_click():
            next_btn = get_element(self.driver, (By.ID, "next-button"))
            next_btn.click()
            rsleep()

        def done_btn_click():
            done_btn = get_element(self.driver, (By.ID, "done-button"))
            done_btn.click()

        visibility = self.get_visibility(visibility)
        self.sing_in()
        self.driver.get("https://studio.youtube.com/channel/upload")

        dismiss_btn = get_element_clickable(self.driver, (By.ID, "dismiss-button"), 5)
        if dismiss_btn:
            dismiss_btn.click()

        create_button = get_element_clickable(self.driver, (By.ID, "create-icon"))
        create_button.click()
        rsleep()

        upload_button = get_element_clickable(self.driver, (By.XPATH, ".//*[@test-id='upload-beta']"))
        upload_button.click()
        rsleep()

        file_input = get_element(self.driver, (By.XPATH, ".//input[@type='file']"))
        file_input.send_keys(video)

        rsleep()

        title_text_area = get_element_clickable(self.driver, (By.ID, "title-textarea"), 60)
        description_text_area = get_element_clickable(self.driver, (By.ID, "description-textarea"))

        not_for_kids_radio_btn = get_element_clickable(self.driver, (By.XPATH,
                                                                     ".//*[@name='VIDEO_MADE_FOR_KIDS_NOT_MFK']"
                                                                     "/div[@id='radioContainer']"))
        title_text_area.send_keys(title)
        rsleep()
        description_text_area.send_keys(description)
        rsleep()
        not_for_kids_radio_btn.click()
        rsleep()

        next_btn_click()
        next_btn_click()
        next_btn_click()

        mark_as_public = get_element(self.driver, (By.XPATH, f".//*[@name='{visibility}']/div[@id='radioContainer']"))
        mark_as_public.click()

        done_btn_click()

    def sing_in(self, deep=0):
        def next_btn_click():
            rsleep()
            next_btn = get_elements(self.driver, (By.TAG_NAME, "button"))[-2]
            next_btn.click()
            rsleep()

        if self.log_in:
            print("Аккаунт авторизирован..")
            return
        elif deep > 2:
            print("Слишком много попыток не удачной авторизации")
            raise CannotSignInError("Ошибка авторизации!")

        self.driver.get("https://accounts.google.com/ServiceLogin/signinchooser")

        account_item = get_element_clickable(self.driver, (By.XPATH,
                                                           ".//div[@data-identifier='heeglewindyqmerid@gmail.com']"))
        use_another_account = get_element_clickable(self.driver, (By.XPATH,
                                                                  ".//div[@data-init-is-remove-mode='0']//li[2]"))
        if account_item:
            account_item.click()
        elif use_another_account:
            use_another_account.click()

        if not account_item:
            email_input = get_element_clickable(self.driver, (By.XPATH, ".//input[@type='email']"))
            send_keys(email_input, self.email)

            next_btn_click()

        password_input = get_element_clickable(self.driver, (By.XPATH, ".//input[@type='password']"))
        if password_input:
            send_keys(password_input, self.password)
            next_btn_click()
        rsleep()

        if not self.log_in:
            print("Повторяем авторизацию..")
            return self.sing_in(deep+1)

        print("Аккаунт авторизирован..")


# def next_btn_click(driver):
#     next_btn = get_element(driver, (By.ID, "next-button"))
#     next_btn.click()
#     rsleep()
#
# def next_btn_click_reg(driver):
#     next_btn = get_elements(driver, (By.TAG_NAME, "button"))[-2]
#     next_btn.click()
#
#
