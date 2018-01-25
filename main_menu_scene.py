# Created by: Kay Lin
# Created on: Jan 2017
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui
import dialogs
import sound
from levels_list_scene import *
from help_scene import *
from setting_scene import *
from credits_scene import *
from bonus_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background
        self.background = SpriteNode('./assets/sprites/main_menu_final.png',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
        
        # check if music is being played or not
        # you can turn on/off the music in setting scene
        if config.music_on == True:
           config.main_menu_music.play()
        elif config.music_on == False:
           config.main_menu_music.pause()
                                         
        start_button_position = Vector2()
        start_button_position.x = self.screen_center_x-290
        start_button_position.y = self.screen_center_y+160                        
        self.start_button = SpriteNode('./assets/sprites/start_button.png',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 1.0)
                                       
        help_button_position = Vector2() 
        help_button_position.x = self.screen_center_x - 290
        help_button_position.y = self.screen_center_y + 50
        self.help_button = SpriteNode('./assets/sprites/help_button.png',
                                       parent = self,
                                       position = help_button_position,
                                       scale = 1.0)
                                       
        credits_button_position = Vector2()
        credits_button_position.x = self.screen_center_x-290
        credits_button_position.y = self.screen_center_y-60              
        self.credits_button = SpriteNode('./assets/sprites/credits_button.png',
                                       parent = self,
                                       position = credits_button_position,
                                       scale = 1.0)
                                                                     
        settings_button_position = Vector2()
        settings_button_position.x = self.screen_center_x-390                     
        settings_button_position.y = self.screen_center_y-170     
        self.settings_button = SpriteNode('./assets/sprites/settings_button.png',
                                         parent = self,
                                         position = settings_button_position,
                                         scale = 1.0)
                                         
        bonus_button_position = Vector2()
        bonus_button_position.x = self.screen_center_x-190
        bonus_button_position.y = self.screen_center_y-170                           
        self.bonus_button = SpriteNode('./assets/sprites/locked_bonus_button.png',
                                       parent = self,
                                       position = bonus_button_position,
                                       scale = 1.0)                                                                                       
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.start_button.frame.contains_point(touch.location):
            config.pressed_home = False
            config.game_over = False
            config.score = 0
            config.blob_hit = 0
            config.squareman_hit = 0
            self.present_modal_scene(LevelsListScene())
            
        # if help button is pressed, goto game scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        
        # if credits button is pressed, goto game scene
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditsScene())
        
        # if setting button is pressed, goto game scene
        if self.settings_button.frame.contains_point(touch.location):
            self.present_modal_scene(SettingScene())
        
        # if bonus button is pressed, goto game scene
        if self.bonus_button.frame.contains_point(touch.location):
            locked = dialogs.alert(title = "Temporarily Locked",
                                   message = "This feature will be locked until the next update where all levels will be added.",
                                   button1 = "OK",
                                   hide_cancel_button = True)
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
