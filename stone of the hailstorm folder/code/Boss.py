from asyncio import events
from turtle import down
import pygame
from player import Player
from support import import_folder

class Boss(pygame.sprite.Sprite):
    def __init__ (self,pos):
        super().__init__()
        self.import_boss_assests()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'idle'

    def import_boss_assests(self):
        boss_path = 'graphics/boss/'
        self.animations = {'idle':[], 'lazer_left':[], 'lazer_right':[], 'damage':[], 'attack_left':[], 'attack_right':[], }

        for animation in self.animations.keys():
            full_path = boss_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        #loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        #240 height
        #1200 width

        if Player == range.rect((0,240),(325,120),(325,0),(0,120)):
            pass

        image = animation[int(self.frame_index)]
        
    def update(self):
        self.animate