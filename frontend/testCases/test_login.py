import pytest
from backend.helpers.api_board import APIBoard

from frontend.helpers.generic import find_element_extended
from backend.helpers.local_configuration import load_config
from frontend.pageObjects.BoardPage import BoardPage
from frontend.pageObjects.LoginPage import LoginPage

test_config = load_config()


class TestLogin():
    base_url = test_config['base_url']
    username = test_config['username']
    password = test_config['password']

    @pytest.mark.second
    def test_objective2(self, setup):
        """
        login test
        :rtype: object
        """
        self.driver = setup
        self.driver.get(self.base_url)
        login = LoginPage(self.driver)
        login.set_username(self.username)
        find_element_extended(LoginPage.button_login, self.driver, 5, 5)
        login.click_login()
        login.set_password(self.password)
        login.click_submit()
        find_element_extended(BoardPage.trello_logo, self.driver, 5, 5)

        board_page = BoardPage(self.driver)
        board_page.select_board_created_through_rest_api_test()

        #  Verify that there are 2 cards on the board
        board_page.verifying_there_are_two_cards_on_the_list(numbers_of_card_to_verify=2)
        #  Verify that there is a card with a comment
        board_page.checking_there_are_any_comments(BoardPage.comments_one_the_card_xpath)
        #  Add new comment
        board_page.add_a_new_comment_to_that_card(board_page.new_comments)

        self.driver.quit()



