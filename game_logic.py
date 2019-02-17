from random import randint
from wizard import Wizard
import pygame
import time




class Game_Logic:
    game_spells = {'burn': 'fire', 'soak': 'water', 'wood': 'earth', 'requiem': 'dark', 'bright': 'light',
                   'heal': 'heal'}
    prefix = {'explosive': 'aoe'}
    elements = {'water': 'fire', 'fire': 'earth', 'earth': 'water', 'light': 'dark', 'dark': 'light'}
    ele_list = {'dark': 'P', 'earth': 'G', 'water': 'B', 'fire': 'R', 'light': 'Y'}


    def __init__(self):
        #Entering massive spaghetti zone
        self.fire_pics = [pygame.image.load('sprites/smallfire1.png'), pygame.image.load('sprites/smallfire2.png')]
        self.water_pics = [pygame.image.load('sprites/smallwater1.png'), pygame.image.load('sprites/smallwater2.png')]
        self.earth_pics = [pygame.image.load('sprites/smallleaf1.png'), pygame.image.load('sprites/smallleaf2.png')]
        self.light_pics = [pygame.image.load('sprites/smalllight1.png'), pygame.image.load('sprites/smalllight2.png')]
        self.dark_pics = [pygame.image.load('sprites/smalldark1.png'), pygame.image.load('sprites/smalldark2.png')]

        self.fire_en = [[eval('pygame.image.load("sprites/{element}en{number}.png")'.format(element = 'fire', number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}ombie{number}.png")'.format(color_letter = Game_Logic.ele_list['fire'], number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}Blob{number}.png")'.format(color_letter = Game_Logic.ele_list['fire'], number = num + 1)) for num in range(2)]]
        self.fire_en_atk = [eval('pygame.image.load("sprites/{element}enatk.png")'.format(element = 'fire')),
            eval('pygame.image.load("sprites/{color_letter}omAttack.png")'.format(color_letter = Game_Logic.ele_list['fire'])),
            eval('pygame.image.load("sprites/{color_letter}BlobAttack.png")'.format(color_letter = Game_Logic.ele_list['fire']))]
        self.fire_en_dead = [eval('pygame.image.load("sprites/{element}endead.png")'.format(element = 'fire')),
            eval('pygame.image.load("sprites/{color_letter}omDead.png")'.format(color_letter = Game_Logic.ele_list['fire'])),
            eval('pygame.image.load("sprites/{color_letter}BlobDead.png")'.format(color_letter = Game_Logic.ele_list['fire']))]

        self.water_en = [[eval('pygame.image.load("sprites/{element}en{number}.png")'.format(element = 'water', number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}ombie{number}.png")'.format(color_letter = Game_Logic.ele_list['water'], number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}Blob{number}.png")'.format(color_letter = Game_Logic.ele_list['water'], number = num + 1)) for num in range(2)]]
        self.water_en_atk = [eval('pygame.image.load("sprites/{element}enatk.png")'.format(element = 'water')),
            eval('pygame.image.load("sprites/{color_letter}omAttack.png")'.format(color_letter = Game_Logic.ele_list['water'])),
            eval('pygame.image.load("sprites/{color_letter}BlobAttack.png")'.format(color_letter = Game_Logic.ele_list['water']))]
        self.water_en_dead = [eval('pygame.image.load("sprites/{element}endead.png")'.format(element = 'water')),
            eval('pygame.image.load("sprites/{color_letter}omDead.png")'.format(color_letter = Game_Logic.ele_list['water'])),
            eval('pygame.image.load("sprites/{color_letter}BlobDead.png")'.format(color_letter = Game_Logic.ele_list['water']))]

        self.earth_en = [[eval('pygame.image.load("sprites/{element}en{number}.png")'.format(element = 'earth', number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}ombie{number}.png")'.format(color_letter = Game_Logic.ele_list['earth'], number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}Blob{number}.png")'.format(color_letter = Game_Logic.ele_list['earth'], number = num + 1)) for num in range(2)]]
        self.earth_en_atk =[eval('pygame.image.load("sprites/{element}enatk.png")'.format(element = 'earth')),
            eval('pygame.image.load("sprites/{color_letter}omAttack.png")'.format(color_letter = Game_Logic.ele_list['earth'])),
            eval('pygame.image.load("sprites/{color_letter}BlobAttack.png")'.format(color_letter = Game_Logic.ele_list['earth']))]
        self.earth_en_dead = [eval('pygame.image.load("sprites/{element}endead.png")'.format(element = 'earth')),
            eval('pygame.image.load("sprites/{color_letter}omDead.png")'.format(color_letter = Game_Logic.ele_list['earth'])),
            eval('pygame.image.load("sprites/{color_letter}BlobDead.png")'.format(color_letter = Game_Logic.ele_list['earth']))]

        self.light_en = [[eval('pygame.image.load("sprites/{element}en{number}.png")'.format(element = 'light', number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}ombie{number}.png")'.format(color_letter = Game_Logic.ele_list['light'], number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}Blob{number}.png")'.format(color_letter = Game_Logic.ele_list['light'], number = num + 1)) for num in range(2)]]
        self.light_en_atk = [eval('pygame.image.load("sprites/{element}enatk.png")'.format(element = 'light')),
            eval('pygame.image.load("sprites/{color_letter}omAttack.png")'.format(color_letter = Game_Logic.ele_list['light'])),
            eval('pygame.image.load("sprites/{color_letter}BlobAttack.png")'.format(color_letter = Game_Logic.ele_list['light']))]
        self.light_en_dead = [eval('pygame.image.load("sprites/{element}endead.png")'.format(element = 'light')),
            eval('pygame.image.load("sprites/{color_letter}omDead.png")'.format(color_letter = Game_Logic.ele_list['light'])),
            eval('pygame.image.load("sprites/{color_letter}BlobDead.png")'.format(color_letter = Game_Logic.ele_list['light']))]

        self.dark_en = [[eval('pygame.image.load("sprites/{element}en{number}.png")'.format(element = 'dark', number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}ombie{number}.png")'.format(color_letter = Game_Logic.ele_list['dark'], number = num + 1)) for num in range(2)],
            [eval('pygame.image.load("sprites/{color_letter}Blob{number}.png")'.format(color_letter = Game_Logic.ele_list['dark'], number = num + 1)) for num in range(2)]]
        self.dark_en_atk = [eval('pygame.image.load("sprites/{element}enatk.png")'.format(element = 'dark')),
            eval('pygame.image.load("sprites/{color_letter}omAttack.png")'.format(color_letter = Game_Logic.ele_list['dark'])),
            eval('pygame.image.load("sprites/{color_letter}BlobAttack.png")'.format(color_letter = Game_Logic.ele_list['dark']))]
        self.dark_en_dead = [eval('pygame.image.load("sprites/{element}endead.png")'.format(element = 'dark')),
            eval('pygame.image.load("sprites/{color_letter}omDead.png")'.format(color_letter = Game_Logic.ele_list['dark'])),
            eval('pygame.image.load("sprites/{color_letter}BlobDead.png")'.format(color_letter = Game_Logic.ele_list['dark']))]

        self.fire_split = [[[eval('pygame.image.load("sprites/Red Enemy Splits/{color}LoadMage{number}.png")'.format(color = 'red', number = num + 1)) for num in range(5)],[eval('pygame.image.load("sprites/Red Enemy Splits/{color}LoadMage{number}a.png")'.format(color = 'red', number = num + 1)) for num in range(5)]],
                    [[eval('pygame.image.load("sprites/Red Enemy Splits/{color}LoadZom{number}.png")'.format(color='red', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Red Enemy Splits/{color}LoadZom{number}a.png")'.format(color='red', number=num + 1)) for num in range(5)]],
                    [[eval('pygame.image.load("sprites/Red Enemy Splits/{color}Load{number}.png")'.format(color='red', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Red Enemy Splits/{color}Load{number}a.png")'.format(color='red', number=num + 1)) for num in range(5)]]]

        self.water_split = [[[eval('pygame.image.load("sprites/Blue Enemy Splits/{color}LoadMage{number}.png")'.format(color = 'blue', number = num + 1)) for num in range(5)],[eval('pygame.image.load("sprites/Blue Enemy Splits/{color}LoadMage{number}a.png")'.format(color = 'blue', number = num + 1)) for num in range(5)]],
                  [[eval('pygame.image.load("sprites/Blue Enemy Splits/{color}LoadZom{number}.png")'.format(color='blue', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Blue Enemy Splits/{color}LoadZom{number}a.png")'.format(color='blue', number=num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Blue Enemy Splits/{color}Load{number}.png")'.format(color='blue', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Blue Enemy Splits/{color}Load{number}a.png")'.format(color='blue', number=num + 1)) for num in range(5)]]]

        self.earth_split = [[[eval('pygame.image.load("sprites/Green Enemy Splits/{color}LoadMage{number}.png")'.format(color = 'green', number = num + 1)) for num in range(5)],[eval('pygame.image.load("sprites/Green Enemy Splits/{color}LoadMage{number}a.png")'.format(color = 'green', number = num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Green Enemy Splits/{color}LoadZom{number}.png")'.format(color='green', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Green Enemy Splits/{color}LoadZom{number}a.png")'.format(color='green', number=num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Green Enemy Splits/{color}Load{number}.png")'.format(color='green', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Green Enemy Splits/{color}Load{number}a.png")'.format(color='green', number=num + 1)) for num in range(5)]]]

        self.light_split = [[[eval('pygame.image.load("sprites/Yellow Enemy Splits/{color}LoadMage{number}.png")'.format(color = 'Yellow', number = num + 1)) for num in range(5)],[eval('pygame.image.load("sprites/Yellow Enemy Splits/{color}LoadMage{number}a.png")'.format(color = 'yellow', number = num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Yellow Enemy Splits/{color}LoadZom{number}.png")'.format(color='Yellow', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Yellow Enemy Splits/{color}LoadZom{number}a.png")'.format(color='yellow', number=num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Yellow Enemy Splits/{color}Load{number}.png")'.format(color='Yellow', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Yellow Enemy Splits/{color}Load{number}a.png")'.format(color='yellow', number=num + 1)) for num in range(5)]]]

        self.dark_split = [[[eval('pygame.image.load("sprites/Purple Enemy Splits/{color}LoadMage{number}.png")'.format(color = 'purple', number = num + 1)) for num in range(5)],[eval('pygame.image.load("sprites/Purple Enemy Splits/{color}LoadMage{number}a.png")'.format(color = 'purple', number = num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Purple Enemy Splits/{color}LoadZom{number}.png")'.format(color='purple', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Purple Enemy Splits/{color}LoadZom{number}a.png")'.format(color='purple', number=num + 1)) for num in range(5)]],
                   [[eval('pygame.image.load("sprites/Purple Enemy Splits/{color}Load{number}.png")'.format(color='purple', number=num + 1)) for num in range(5)], [eval('pygame.image.load("sprites/Purple Enemy Splits/{color}Load{number}a.png")'.format(color='purple', number=num + 1)) for num in range(5)]]]

        self.boxes = [pygame.image.load('sprites/RedBox1.png'), pygame.image.load('sprites/RedBox2.png')]

        self.spawn_locations = [(205, 160), (110, 260), (310, 260)]
        #Did you enjoy your fine Italian dinner?

    def check_valid_spell(self, m_c, spell, target):
        if spell in m_c.game_spells:
            m_c.exec_turn(target, spell)
        else:
            m_c.mistake()

    def check_valid_prefix_spell(self, m_c, prefix, spell, targets, target_num):
        if spell in m_c.game_spells and prefix in Wizard.game_prefixes:
            m_c.exec_turn(targets[target_num], spell)
            if prefix == 'ledo magis hosti':
                for target in targets:
                    m_c.exec_aoe(target, spell)
            elif prefix == 'sonticus':
                m_c.exec_boost(targets[target_num], spell)
        else:
            m_c.mistake()

    def ai_constant_attack(self, screen, enemy_party, m_c):
        for count, enemy in enumerate(enemy_party):
            self.ai_choose_spell( enemy, m_c)

    def ai_choose_spell(self, enemy, m_c):
        if enemy.element is 'fire':
            spell = 'ambustum'
        elif enemy.element is 'water':
            spell = 'macerari'
        elif enemy.element is 'earth':
            spell = 'planicia'
        elif enemy.element is 'light':
            spell = 'opscurum'
        elif enemy.element is 'dark':
            spell = 'illustris'
        if self.health_is_gt_0(enemy):
            enemy.exec_turn(m_c, spell)

    def health_is_gt_0(self, unit):
        if unit.hp > 0:
            return True
        return False

    def all_enemies_dead(self, enemy_party):
        return all([(not self.health_is_gt_0(enemy)) for enemy in enemy_party])

    def new_enemies(self, level, text_box, difficulty_scaling):
            return [Wizard([element for element in Game_Logic.elements][randint(0,4)], level // 2,text_box) for i in range(randint(1, difficulty_scaling))] #



    def update_screen(self, screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic): #animation
          #may move into settings
        #exec("screen.blit(self.{element}_pics[wizard_element_pic // 15], (277, 224))".format(element=character_party[0].element))
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.blit(self.{element}_pics[current_pics[i] // 15], {spawn})".format(element=enemy_party[i].element, spawn=(self.spawn_locations[i][0] + 25, self.spawn_locations[i][1] - 50)))
                exec("screen.blit(self.{element}_en[{monster_type}][current_pics[i]//15], {spawn})".format(element = enemy_party[i].element, monster_type = enemy_party[i].monster_type, spawn=self.spawn_locations[i]))
                exec("screen.blit(self.{element}_en[enemy_party[i].monster_type][current_pics[i]//15], {spawn})".format(element = enemy_party[i].element, spawn=self.spawn_locations[i]))
            else:
                exec("screen.blit(self.{element}_en_dead[enemy_party[i].monster_type], {spawn})".format(element=enemy_party[i].element, spawn=self.spawn_locations[i]))
        screen.blit(self.boxes[current_pics[1] // 15], (self.spawn_locations[target_num][0] - 10, self.spawn_locations[target_num][1] - 50))
        exec("screen.blit(self.{element}_pics[wizard_element_pic // 15], (277, 224))".format(element=character_party[0].element))

    def update_screen_attacking(self, screen, character_party, enemy_party, current_pics, target_num, wizard_element_pic, spellbook, shifting): #animation
          #may move into settings
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.blit(self.{element}_pics[current_pics[i] // 15], {spawn})".format(element = enemy_party[i].element, spawn=(self.spawn_locations[i][0] + 25, self.spawn_locations[i][1] - 50)))
                exec("screen.blit(self.{element}_en_atk[{monster_type}], {spawn})".format(element = enemy_party[i].element, monster_type = enemy_party[i].monster_type, spawn=self.spawn_locations[i]))
            else:
                exec("screen.blit(self.{element}_en_dead[enemy_party[i].monster_type], {spawn})".format(element=enemy_party[i].element, spawn=self.spawn_locations[i]))
        screen.blit(self.boxes[current_pics[1] // 15], (self.spawn_locations[target_num][0] - 10, self.spawn_locations[target_num][1] - 50))
        exec("screen.blit(self.{element}_pics[wizard_element_pic // 15], (277, 224))".format(element=character_party[0].element))
        if shifting:
            spellbook.open(screen)

    def key_LR(self, event, target_num, enemy_party):    #moves the target and red box
        tn = target_num
        if event.key == pygame.K_RIGHT:
            tn += 1
            if tn > len(enemy_party) - 1:
                tn = 0
            while(not self.health_is_gt_0(enemy_party[tn])):
                tn += 1
                if tn > len(enemy_party) - 1:
                    tn = 0
            return tn
        elif event.key == pygame.K_LEFT:
            tn -= 1
            if tn < 0:
                tn = len(enemy_party) - 1
            while (not self.health_is_gt_0(enemy_party[tn])):
                tn -= 1
                if tn < 0:
                    tn = len(enemy_party) - 1
            return tn

    def LR_change(self, target_num, enemy_party):
        tn = target_num
        while not self.health_is_gt_0(enemy_party[tn]):
            tn += 1
            if tn == len(enemy_party):
                tn = 0
        return tn

    def gen_new_level(self, level_num, enemy_party): #returns a new enemy party list when the one in the current level has died
        for i in range(5):
            enemy_party.append(Wizard([element for element in Game_Logic.elements][randint(0,4)], level_num // 2))
        return enemy_party

    def update_HP_bar(self, screen, m_c):
        m_c_hp = m_c.hp
        HP_bar = pygame.Rect((50, 420 - 200*(m_c_hp / m_c.max_hp)), (15, 200*(m_c_hp / m_c.max_hp)))
        screen.blit(pygame.image.load('sprites/heart.png'), (45, 420))
        screen.fill((255, 100, 100), HP_bar)

    def update_enemy_HP_bar(self, screen, enemy_party):
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.fill((255,100,100), pygame.Rect({spawn}, (({enemy}.hp/{enemy}.max_hp) * 40, 6)))".format(
                        enemy='enemy_party[i]', spawn=(self.spawn_locations[i][0] + 30, self.spawn_locations[i][1] + 100)))

    def update_enemy_atk_bar(self, screen, enemy_party, time_counter):
        for i in range(len(enemy_party)):
            if self.health_is_gt_0(enemy_party[i]):
                exec("screen.fill((255,255,0), pygame.Rect({spawn}, ({time_counter} * 5, 2)))".format(time_counter=str(time_counter // 1000), spawn=(self.spawn_locations[i][0] + 30, self.spawn_locations[i][1] + 98)))

    def spawn_enemies(self, screen, enemy_party, current_pics, row): #HERE
        for i in range(len(enemy_party)):
            exec("screen.blit(self.{element}_split[enemy_party[i].monster_type][current_pics[i] // 15][row], {spawn})".format(element=enemy_party[i].element, spawn=self.spawn_locations[i]))
