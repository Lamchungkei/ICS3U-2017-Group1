# Created by: Kay Lin
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui

from main_menu_scene import *

class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
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
                                       
        #self.help_info = LabelNode(text = "Use the shoot button to blast those nasty blobs away with algebra.",
                                   #font = ('Menlo-Bold', 40),
                                   #color = 'white',
                                   #parent = self,
                                   #position = self.size)
        
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
        
        # if back button is pressed, goto main menu scene
        if self.back_button.frame.contains_point(touch.location):
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
    
