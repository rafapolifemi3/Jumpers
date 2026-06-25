# -- coding: utf-8 --
import pygame.display

from entity import Entity
from entityFactory import EntityFactory


class Demo:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Demo1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass