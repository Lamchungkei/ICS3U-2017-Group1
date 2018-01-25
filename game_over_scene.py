# Created by: Kay Lin
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the game over scene.

from scene import *
import ui
import config

from main_menu_scene import *
#from level_1 import *

class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background color
        self.background = SpriteNode('./assets/sprites/game_over_temp.png',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
                                     
        home_button_position = Vector2()
        home_button_position.x = self.screen_center_x + 350
        home_button_position.y = self.screen_center_y + 150
        self.home_button = SpriteNode('./assets/sprites/main_menu_simple_button.png',
                                      parent = self,
                                      position = home_button_position,
                                      scale = 1.0)            
        
        retry_button_position = Vector2()
        retry_button_position.x = self.screen_center_x + 125
        retry_button_position.y = self.screen_center_y + 150
        self.retry_button = SpriteNode('./assets/sprites/retry_button.png',
                                       parent = self,
                                       position = retry_button_position,
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
        
        # if home button is pressed, goto MainMenuScene scene
        if self.home_button.frame.contains_point(touch.location):
            config.game_over = True
            self.dismiss_modal_scene()
            
        # if retry button is pressed, restart the game
        if self.retry_button.frame.contains_point(touch.location):
            config.pressed_home = False
            config.game_over = False
            config.retry = True
            config.score = 0
            config.blob_hit = 0
            config.squareman_hit = 0
            
            self.dismiss_modal_scene()
            
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
    
