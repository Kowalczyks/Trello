from backend.helpers.rest_api_helper import RestApiHelper
from backend.helpers.local_configuration import load_config

test_config = load_config()


class APIBoard:

    def __init__(self):
        self.base_url = test_config['api_trello_host']
        self.rest_api_helper = RestApiHelper()

    def create_board_call(self, board_name):
        create_board = self.rest_api_helper.post_call(
            self.base_url + f'/boards?defaultLists=false&' + f'name={board_name}' + '&' + 'key=' + test_config[
                'key'] + '&' + 'token=' + test_config['token'] + '&' + 'secret=' + test_config['secret'],
            headers=None)

        assert create_board.status_code == 200, 'Create board status code is different than 200!!'

        return create_board.json()

    def get_call(self):
        get = self.rest_api_helper.get_call(
            endpoint=self.base_url + f'/members/me/boards?fields=DKW&' + 'key=' + test_config['key'] + '&' + 'token=' +
                     test_config['token'], headers=None)

        return get

    def delete_board_call(self, board_id):
        delete_board = self.rest_api_helper.delete_call(
            self.base_url + f'/boards/' + f'{board_id}' + '?' + 'key=' + test_config[
                'key'] + '&' + 'token=' + test_config['token'] + '&' + 'secret=' + test_config['secret'],
            headers=None)

        return delete_board

    def create_a_list_on_a_board_call(self, list_name, id_board):
        create_list = self.rest_api_helper.post_call(
            self.base_url + '/lists?' + 'key=' + test_config[
                'key'] + '&' + 'token=' + test_config[
                'token'] + '&' + f'name={list_name}' + '&' + f'idBoard={id_board}',
            headers=None)

        return create_list.json()

    def create_card_on_the_board_call(self, id_list, card_count, card_name):
        global create_card
        responses = []
        for i in range(card_count):
            create_card = self.rest_api_helper.post_call(
                self.base_url + '/cards?' + 'key=' + test_config[
                    'key'] + '&' + 'token=' + test_config[
                    'token'] + '&' + f'idList={id_list}' + '&' + f'name={card_name}', headers=None)
            responses.append(create_card)
        return responses

    def update_card_call(self, card_id, new_card_name):
        update_card = self.rest_api_helper.put_call(
            self.base_url + '/cards/' + f'{card_id}' + '?' + 'key=' + test_config[
                'key'] + '&' + 'token=' + test_config[
                'token'] + '&' + f'name={new_card_name}', headers=None)
        return update_card.json()

    def delete_card_call(self, card_id):
        delete_card = self.rest_api_helper.delete_call(
            self.base_url + '/cards/' + f'{card_id}' + '?' + 'key=' + test_config[
                'key'] + '&' + 'token=' + test_config[
                'token'], headers=None)
        return delete_card.json()

    def add_comment_to_the_card(self, card_id, comments):
        comment_card = self.rest_api_helper.post_call(
            self.base_url + '/cards/' + f'{card_id}' + '/actions/' + 'comments?' + 'key=' + test_config[
                'key'] + '&' + 'token=' + test_config[
                'token'] + '&' + f'text={comments}', headers=None)
        return comment_card.json()
