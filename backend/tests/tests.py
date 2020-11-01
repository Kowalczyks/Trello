
import time
import pytest
from colorama import Fore
from backend.helpers.api_board import APIBoard
from backend.helpers.local_configuration import load_config
from backend.helpers.logger import Logger

test_config = load_config()


@pytest.mark.first
def test_objective1():
    """
    change board_name to any string, thus will add board with specified name on to trello
    :return:
    """
    # create board
    api_board = APIBoard()
    board_name = test_config['board_name']
    create_board = api_board.create_board_call(board_name=board_name)
    Logger.LogInfo(f"{Fore.LIGHTRED_EX} creating a board named {create_board['name']}")
    assert create_board['name'] == board_name, "Board names are different!"

    # test_create_list
    """
    change list name to any string, thus will and new list name on to the board 
    """
    list_name = 'some_list'
    create_list_on_the_board = api_board.create_a_list_on_a_board_call(list_name=list_name, id_board=create_board['id'])
    Logger.LogInfo(
        f'{Fore.LIGHTRED_EX} creating list named {list_name} and list_id {create_list_on_the_board["id"]} on the board_id {create_board["id"]}')
    assert create_list_on_the_board['name'] == list_name, 'List names are different!!'

    # create card on the board
    """
    change card count to any int thus will add proper number of a cards in to the board
    """
    card_count = 3
    card_name = 'someCard'
    create_card_on_the_board = api_board.create_card_on_the_board_call(id_list=create_list_on_the_board["id"],
                                                                       card_count=card_count, card_name=card_name)
    Logger.LogInfo(
        f'{Fore.LIGHTRED_EX} creating card named {card_name}, with id_list as {create_list_on_the_board["id"]} and card count as {card_count}')
    assert create_card_on_the_board[0].json()['name'] == card_name, "Card name is different than response card name"

    # update name of the card
    """
    change new_card_number to any string, thus will update last card name
    """
    new_card_name = 'NewCardName2'
    update_card = api_board.update_card_call(card_id=create_card_on_the_board[0].json()['id'],
                                             new_card_name=new_card_name)
    Logger.LogInfo(
        f'{Fore.LIGHTRED_EX} updating card with id as {create_card_on_the_board[0].json()["id"]} and new name as {new_card_name}')
    assert new_card_name == update_card['name'], 'Card name differs !!'

    # added comment to the card
    """
    to add comment to the last card change string value
    """
    comments = "this is a new comment"
    add_comment_to_the_card = api_board.add_comment_to_the_card(card_id=create_card_on_the_board[0].json()['id'],
                                                                comments=comments)
    Logger.LogInfo(
        f'{Fore.LIGHTRED_EX} Comments such like {comments} added to card id {create_card_on_the_board[0].json()["id"]}')

    time.sleep(5)
    Logger.LogInfo(f'{Fore.CYAN} Now we waiting just to show that the new comment was added to the card before delete')
    time.sleep(5)

    # delete card
    """
    to delete last card use method below
    """
    delete_card = api_board.delete_card_call(card_id=create_card_on_the_board[1].json()['id'])
    Logger.LogInfo(f'deleting card with id as {create_card_on_the_board[1].json()["id"]}')

    # delete board
    """
    this method deletes any specific board from trello,
    """
    board_id = create_board['id']
    delete_board = api_board.delete_board_call(board_id=board_id)
    assert delete_board.status_code == 200, f"Status code is {delete_board.status_code} is not what we expect"
