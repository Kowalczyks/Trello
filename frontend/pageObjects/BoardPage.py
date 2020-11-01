import time

from colorama import Fore
from selenium.common.exceptions import NoSuchElementException
from backend.helpers.api_board import test_config
from backend.helpers.logger import Logger
from frontend.helpers.generic import find_element_extended


class BoardPage():
    create_board_button = '//div[@class="board-tile mod-add"]'
    add_board_title = '//input[@placeholder="Add board title"]'
    create_board_green = '//button[text()="Create Board"]'
    trello_logo = '//*[@id="header"]/a/div[1]/span[2]'
    card_list_xpath = '//a[@class="list-card js-member-droppable ui-droppable"]'
    comments_one_the_card_xpath = '//div[@title="Comments"]'
    select_card_xpath = '//span[text()="someCard"]'
    write_comments_field_xpath = '//textarea[@placeholder="Write a comment…"]'
    new_comments = "newComment"
    save_comment_button = "//input[@class='primary confirm mod-no-top-bottom-margin js-add-comment']"

    def __init__(self, driver):
        self.driver = driver

    def click_create_new_board_from_main_page(self):
        self.driver.find_element_by_xpath(self.create_board_button).click()

    def add_board_title_on_the_board(self, title):
        self.driver.find_element_by_xpath(self.add_board_title).send_keys(title)

    def click_create_board_green_button(self):
        self.driver.find_element_by_xpath(self.create_board_green).click()

    def select_board_created_through_rest_api_test(self):
        try:
            board_xpath = f'//div[@title="{test_config["board_name"]}"]'
            find_element_extended(board_xpath, self.driver, 3, 3)
            last_board = self.driver.find_element_by_xpath(board_xpath)
            last_board.click()
        except NoSuchElementException:
            Logger.LogInfo(f"{Fore.RED}There is no board created, please run backend test for create a board")
            quit()

    def verifying_there_are_two_cards_on_the_list(self, numbers_of_card_to_verify):
        find_element_extended(self.card_list_xpath, self.driver, 3, 3)
        card_list = self.driver.find_elements_by_xpath(self.card_list_xpath)
        if len(card_list) == numbers_of_card_to_verify:
            Logger.LogInfo(f"{Fore.GREEN} Success!! there are exactly two cards on the list")
        else:
            Logger.LogInfo(f" The number of cards is not as expected because it is {len(card_list)} ")
            self.driver.save_screenshot(".\\frontend\\screen_shots\\" + "verifying_two_cards_on_the_list.png")

    def checking_there_are_any_comments(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            Logger.LogInfo(" There is no comments on the card")
            return False
        Logger.LogInfo(" Success there is a comment on the card")
        return True

    def add_a_new_comment_to_that_card(self, comment):
        select_card = self.driver.find_element_by_xpath(self.select_card_xpath)
        select_card.click()
        find_element_extended(self.write_comments_field_xpath, self.driver, 5, 5)
        self.driver.find_element_by_xpath(self.write_comments_field_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.write_comments_field_xpath).send_keys(self.new_comments)
        self.driver.find_element_by_xpath(self.save_comment_button).click()
