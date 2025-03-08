import unittest
from unittest.mock import patch, MagicMock
from romanGame.menu_functions import new_Game, displaySaveGames
from common_functions import load_characters
from styles import narrator_print

class TestGameFunctions(unittest.TestCase):

    @patch('builtins.input', return_value='Maximus')
    @patch('os.system')  # Mock os.system to avoid clearing the console
    @patch('questionary.select')  # Mock questionary.select
    @patch('questionary.select.ask') # Mock questionary.select.ask
    @patch('common_functions.load_characters')  # Mock file loading function
    @patch('common_functions.save_characters')  # Mock file saving function
    @patch('styles.narrator_print')  # Mock narrator_print to avoid printing in tests
    def test_new_game(self, mock_narrator, mock_save, mock_load, mock_select, mock_system, mock_input):
        # Set up mock return values
        mock_select.return_value = 'The Scipius family'
        mock_load.return_value = []  # No saved characters
        mock_narrator.return_value = None  # Mock print function

        # Call the new_game function
        console = MagicMock()  # Mock the console object
        new_Game(console)

        # Assertions
        mock_input.assert_any_call(">   ")  # Ensure input is being called for player name
        mock_select.assert_called_once_with('', choices=["The Scipius family", "The Julian family", "The Claudius family", "The Flavius family", "I belong to no family.(Warning, this sets the game on the highest difficulty. Only for veteran players.)"])
        mock_save.assert_called_once()  # Ensure save function is called
        mock_load.assert_called_once()  # Ensure load function is called

    @patch('common_functions.load_characters')
    @patch('styles.narrator_print')
    @patch('questionary.select')
    @patch('os.system')
    def test_display_save_games_no_saves(self, mock_select, mock_narrator, mock_load, mock_system):
        mock_load.return_value = []  # No saved characters

        console = MagicMock()
        displaySaveGames(console)

        mock_narrator.assert_called_with("It seems like you haven't yet saved any Romans. Go back to the menu and start a new game!", console)
        
    @patch('common_functions.load_characters')
    @patch('styles.narrator_print')
    @patch('questionary.select')
    def test_display_save_games_with_saves(self, mock_select, mock_narrator, mock_load):
        # Simulate saved characters
        mock_load.return_value = [
            {'id': 1, 'first_name': 'Maximus', 'family_name': 'Scipio', 'level': 1},
            {'id': 2, 'first_name': 'Julius', 'family_name': 'Caesar', 'level': 5}
        ]

        mock_select.return_value = 'Maximus Scipio'

        console = MagicMock()
        displaySaveGames(console)

        # Check that the correct select choice was made
        mock_select.assert_called_once_with('', choices=['Maximus Scipio', 'Julius Caesar'])
        mock_narrator.assert_called_once()  # Ensure narrator_print was called
        

if __name__ == '__main__':
    unittest.main()