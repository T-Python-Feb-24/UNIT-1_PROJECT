import json
from prettytable import PrettyTable
import shutil
from color import Color
from colorama import Fore
from art import *
class Player:
    def load_player_data(player_data):
        try:
            with open("players_data.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def store_player_data(player_data):
        with open("players_data.json", "w", encoding="utf-8") as file:
            json.dump(player_data, file, indent=2)
        #print("Data saved successfully.")

    def player_exists(player_name,player_data): # لو كان اللاعب موجود قبل كددا 
        for player in player_data:
            if player["name"].lower() == player_name.lower():
                return player
        return None

    def display_leaderboard_pretty(player_data):
        # Create a PrettyTable instance
        table = PrettyTable()
        # Add columns
        table.field_names = ["  Rank  ", "  Name  ", "  Score  "]
        
        # Sort players by score in descending order
        sorted_players = sorted(player_data, key=lambda x: x['score'], reverse=True)
        
        # Add rows to the table
        for i, player in enumerate(sorted_players, 1):
            table.add_row([i, player['name'], player['score']])
        
        # Convert table to string
        table_str = str(table)
        
        # Calculate terminal size
        terminal_size = shutil.get_terminal_size()
        terminal_width = terminal_size.columns
        terminal_height = terminal_size.lines
        
        # Calculate table size
        table_lines = table_str.split('\n')
        table_width = max(len(line) for line in table_lines)
        table_height = len(table_lines)
        
        # Calculate padding
        vertical_padding = max((terminal_height - table_height) // 7, 0)
        horizontal_padding = max((terminal_width - table_width) // 7, 0)
        
        # Print the table with padding
        print()
        print(Color.color_code_yellow + " " * 22 + "    🎖️ 🎖️ 🎖️ LEADERBOARD 🎖️ 🎖️ 🎖️")
        print()
        for line in table_lines:
            print(" " * horizontal_padding + line)
        print()
