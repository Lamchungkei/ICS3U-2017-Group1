# Created by: Kay Lin
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the setting scene.

from scene import *
import ui
import sound
import config
from main_menu_scene import *

class SettingScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # music is be played or not
        # you can turn on/off the music in setting scene
        if config.music_on == True:
           config.main_menu_music.number_of_loops = -1
           config.main_menu_music.play()
        elif config.music_on == False:
           config.main_menu_music.pause()
           
           
        # add background color
        self.background = SpriteNode('./assets/sprites/background_standard.png',
                                     position = self.size/2, 
                                     parent = self, 
                                     size = self.size)
                                     
        back_button_position = Vector2()
        back_button_position.x = self.screen_center_x - 440
        back_button_position.y = self.screen_center_y + 300               
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.9)
                                     
        sound_on_button_position = Vector2()
        sound_on_button_position.x = self.screen_center_x - 100
        sound_on_button_position.y = self.screen_center_y + 250
        self.sound_on_button = SpriteNode('./assets/sprites/sound_on_button.png',
                                          parent = self,
                                          position = sound_on_button_position,                                                               
                                          scale = 0.8)       
        
        sound_off_button_position = Vector2()
        sound_off_button_position.x = self.screen_center_x + 100
        sound_off_button_position.y = self.screen_center_y + 250
        self.sound_off_button = SpriteNode('./assets/sprites/sound_off_button.png',
                                           parent = self,
                                           position = sound_off_button_position,
                                           scale = 0.8)  
        # squareman skins
        skins_choose_label_position = Vector2()
        skins_choose_label_position.x = self.screen_center_x - 300
        skins_choose_label_position.y = self.screen_center_y
        self.skins_choose_label = LabelNode(text = "SKINS:",
                                            font = ('Menlo-Bold', 40),
                                            color = 'white',
                                            parent = self,
                                            position = skins_choose_label_position)
                                    
        original_skin_position = Vector2()
        original_skin_position.x = self.screen_center_x - 50
        original_skin_position.y = self.screen_center_y - 12
        self.original_skin = SpriteNode('./assets/sprites/skins/original.png',
                                        parent = self,
                                        position = original_skin_position,
                                        scale = 1.0)
        
        flashback_skin_position = Vector2()
        flashback_skin_position.x = self.screen_center_x + 70
        flashback_skin_position.y = self.screen_center_y - 12
        self.flashback_skin = SpriteNode('./assets/sprites/skins/flashback.png',
                                         parent = self,
                                         position = flashback_skin_position,
                                         scale = 1.0)
                                        
        panda_skin_position = Vector2()
        panda_skin_position.x = self.screen_center_x + 190
        panda_skin_position.y = self.screen_center_y - 12
        self.panda_skin = SpriteNode('./assets/sprites/skins/panda.png',
                                        parent = self,
                                        position = panda_skin_position,
                                        scale = 1.0)
         
        poker_skin_position = Vector2()
        poker_skin_position.x = self.screen_center_x + 310
        poker_skin_position.y = self.screen_center_y - 12
        self.poker_skin = SpriteNode('./assets/sprites/skins/poker.png',
                                     parent = self,
                                     position = poker_skin_position,
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
        
        # if back button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        
        # if sound_on button is pressed, turn on the music
        if self.sound_on_button.frame.contains_point(touch.location):
            config.main_menu_music.play()
            config.music_on = True
            
        # if sound_off button is pressed, turn off the music
        if self.sound_off_button.frame.contains_point(touch.location):
            config.main_menu_music.pause()
            config.music_on = False
            
        # changing skins options
        if self.original_skin.frame.contains_point(touch.location):
            config.skin_settings = 'original'
        
        if self.flashback_skin.frame.contains_point(touch.location):
            config.skin_settings = 'flashback'
        
        if self.panda_skin.frame.contains_point(touch.location):
            config.skin_settings = 'panda'
        
        if self.poker_skin.frame.contains_point(touch.location):
            config.skin_settings = 'poker'
        
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
    
