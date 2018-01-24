# Created by: Kay Lin
# Created on: Jan 2018
# Created for: ICS3U
# This holds all global variables.

import sound

score = 0
high_score = 0
blob_hit = 0
skin_settings = 'original'
pressed_pause = False
music_on = True
game_over = False
game_win = False
main_menu_music = sound.Player('assets/sounds/Squareland.wav')
game_over_music = sound.Player('assets/sounds/Probably Game Over (Loop).wav')
#game_win_music = sound.Player('assets/sounds/')
