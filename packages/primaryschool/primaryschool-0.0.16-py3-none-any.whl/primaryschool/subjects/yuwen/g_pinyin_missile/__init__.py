import copy
import os
import pickle
import random
import sys
from datetime import datetime, timedelta
from typing import Any, List, Optional, Sequence, Text, Tuple, Union, overload

import pygame
import pygame_menu
from pygame.key import key_code
from pygame.locals import *
from xpinyin import Pinyin

from primaryschool.dirs import *
from primaryschool.locale import _
from primaryschool.resource import (default_font, default_font_path,
                                    get_default_font, get_font_path,
                                    get_resource_path)
from primaryschool.subjects import *
from primaryschool.subjects._abc_ import GameBase
from primaryschool.subjects.yuwen.words import cn_ps_c, cn_ps_c_bb

# primaryschool.subjects.yuwen.g_pinyin_missile
module_str = __name__

name_t = _('Pinyin Missile')

default_difficulty_index = 16
difficulties = [
    _('Grade 1.1'),  # 0
    _('Grade 1.2'),  # 1
    _('Grade 2.1'),  # 2
    _('Grade 2.2'),  # 3
    _('Grade 3.1'),  # 4
    _('Grade 3.2'),  # 5
    _('Grade 4.1'),  # 6
    _('Grade 4.2'),  # 7
    _('Grade 5.1'),  # 8
    _('Grade 5.2'),  # 9
    _('Grade 6.1'),  # 10
    _('Grade 6.2'),  # 11
    _('Low level'),  # 12
    _('High level'),  # 13
    _('All grades'),  # 14
    _('All Chinese characters'),  # 15
    _('Grade 1.1 (30 characters)'),  # 16
    _('Grade 1.2 (30 characters)'),  # 17
    _('Grade 2.1 (30 characters)'),  # 18
    _('Grade 2.2 (30 characters)'),  # 19
    _('Grade 3.1 (30 characters)'),  # 20
    _('Grade 3.2 (30 characters)'),  # 21
    _('Grade 4.1 (30 characters)'),  # 22
    _('Grade 4.2 (30 characters)'),  # 23
    _('Grade 5.1 (30 characters)'),  # 24
    _('Grade 5.2 (30 characters)'),  # 25
    _('Grade 6.1 (30 characters)'),  # 26
    _('Grade 6.2 (30 characters)'),  # 27
    _('Low level (30 characters)'),  # 28
    _('High level (30 characters)'),  # 29
    _('All grades (30 characters)'),  # 30
    _('All Chinese characters (30 characters)'),  # 31

]

help_t = _('''
Enter the pinyin corresponding to the Chinese character, and enter the number
after the pinyin to indicate the tone.
''')

pinyin = Pinyin()

cn_ps_chars = cn_ps_c_bb


class Word():
    def __init__(self, pm):
        self.pm = pm
        self.ps = self.pm.ps
        self.rand_word_count = 70
        pass

    def get_words(self, g_index: int):
        _base_len = int(len(difficulties) / 2)
        if g_index < _base_len:
            if g_index == _base_len - 1:
                return self.get_rand_words(self.rand_word_count)
            if 0 <= g_index < _base_len - 1:
                return self.get_cn_ps_words(g_index)
        else:
            g_index = g_index - _base_len
            if g_index == _base_len - 1:
                return random.choices(
                    self.get_rand_words(self.rand_word_count), k=30)
            if 0 <= g_index < _base_len - 1:
                return random.choices(
                    self.get_cn_ps_words(g_index), k=30)

    def get_cn_ps_words(self, g_index: int):
        words = []
        if g_index < 12:
            words = cn_ps_chars[g_index]
        elif g_index == 12:
            words = sum(cn_ps_chars[0:6], [])
        elif g_index == 13:
            words = sum(cn_ps_chars[6:16], [])
        elif g_index == 14:
            words = sum(cn_ps_chars[0:16], [])
        return sum(words, [])

    def get_rand_words(self, n):
        return [chr(random.randint(0x4e00, 0x9fbf)) for i in range(0, n)]


class Wave():
    def __init__(self, pm):
        self.pm = pm
        self.ps = self.pm.ps
        self.intercept_interval = \
            self.pm.wordsurfaces_manager.intercept_interval
        self.surface = self.pm.surface
        self.w_height = self.pm.w_height
        self.w_height_of_2 = self.pm.w_height_of_2
        self.w_width_of_2 = self.pm.w_width_of_2
        self.w_centrex_y = self.pm.w_centrex_y
        self.color = (0, 255, 0, 20)
        self.width = 5

        self.max_radius = self.get_max_radius()

    def set_color(self, color):
        self.color = color

    def get_max_radius(self):
        return (self.w_height**2 + self.w_width_of_2**2)**0.5

    def set_width(self, width):
        assert isinstance(width, int)
        self.width = widgets

    def draw(self, frame_counter):
        if frame_counter >= self.intercept_interval:
            return
        _radius = self.max_radius / (self.intercept_interval - frame_counter)
        pygame.draw.circle(self.surface, self.color,
                           self.w_centrex_y, _radius, width=self.width)


class InputSurface():
    def __init__(self, pm):
        self.pm = pm
        self.ps = self.pm.ps
        self.font_size = 55
        self.font = get_default_font(self.font_size)
        self.surface_color = (200, 22, 98)
        self.surface_bg_color = (200, 100, 100, 89)
        self.surface_bg_border_radius = 10
        self.surface_bg_width = 2
        self.surface = None
        self.frame_counter = 0

    def _update(self):
        self.surface = self.font.render(
            self.pm._input, False, self.surface_color)

    def blit(self):
        if self.surface is None:
            return
        w, h = self.surface.get_size()
        _dest = (self.pm.w_width_of_2 - w / 2, self.pm.w_height - h)
        _surface_size = self.surface.get_size()
        _bg_rect = (_dest[0], _dest[1], _surface_size[0], _surface_size[1])
        pygame.draw.rect(self.pm.surface, color=self.surface_bg_color,
                         width=self.surface_bg_width, rect=_bg_rect,
                         border_radius=self.surface_bg_border_radius)
        self.pm.surface.blit(
            self.surface, _dest)


class WallSurface():
    def __init__(self, pm):
        self.pm = pm
        self.ps = self.pm.ps
        self.h = self.pm.w_height / 20
        self.surface = pygame.Surface((self.pm.w_width, self.h))
        self.color = self.get_default_color()
        self.emitter_radius = self.h / 2
        self.emitter_color = None
        self.center = self.get_center()
        self.flicker_interval = 1 * self.ps.FPS  # 2s
        self.flicker_counter = 0
        self.flicker_color = [self.color, (250, 0, 0)]
        self.flicker_color_step = (
            (self.flicker_color[1][0] - self.flicker_color[0][0])
            / self.flicker_interval,
            (self.flicker_color[1][1] - self.flicker_color[0][1])
            / self.flicker_interval,
            (self.flicker_color[1][2] - self.flicker_color[0][2])
            / self.flicker_interval,
        )

    def get_default_color(self):
        return (10, 200, 99)

    def flicker(self):
        self.flicker_counter += 1
        self.color = (
            min(
                int(self.flicker_color[0][0]
                    + self.flicker_color_step[0] * self.flicker_counter),
                255),
            min(
                int(self.flicker_color[0][1]
                    + self.flicker_color_step[1] * self.flicker_counter),
                255),
            min(
                int(self.flicker_color[0][2]
                    + self.flicker_color_step[2] * self.flicker_counter),
                255)
        )
        if self.flicker_counter >= self.flicker_interval:
            self.flicker_counter = 0
            self.color = self.get_default_color()
        return self.flicker_counter

    def set_emitter_color(self, color=(255, 0, 0, 50)):
        self.emitter_color = color

    def get_emitter_color(self):
        return self.emitter_color

    def get_center(self):
        return [self.ps.w_width_of_2, self.ps.w_height - self.h / 2]

    def draw_emitter(self):
        self.emitter_color = self.set_emitter_color() \
            if self.pm.wordsurfaces_manager is None \
            else self.pm.wordsurfaces_manager.laser_color
        pygame.draw.circle(self.ps.surface, self.emitter_color,
                           self.center, self.emitter_radius)

    def blit(self):
        self.surface.fill(self.color)
        self.pm.surface.blit(self.surface, (0, self.pm.w_height - self.h))
        self.draw_emitter()


class WordSurfacesManager():
    def __init__(self, pm, frame_counter=0):
        self.pm = pm
        self.words = self.pm.words
        self.ps = self.pm.ps
        self.moving_surfaces = []
        self.frame_counter = frame_counter
        self.interval = 3.5 * self.pm.FPS
        self.intercept_interval = 0.3 * self.pm.FPS
        self.moving_speed = 0.5
        self.intercepted_color = (175, 10, 175, 100)
        self.laser_color = (0, 0, 255, 90)
        self.laser_width = 2
        self.font_size = 50
        self.lang_code = 'zh_CN'
        self.font_path = get_font_path(self.lang_code, show_not_found=True)
        self.font = pygame.font.Font(self.font_path, self.font_size)
        self.surfaces = []

    def set_font_size(self, size):
        assert isinstance(size, int)
        self.font_size = size

    def get_font_size(self):
        return self.font_size

    def set_surfaces(self):
        assert len(self.words) > 0
        self.surfaces = [WordSurface(self.pm, self, w) for w in self.words]

    def get_surfaces(self):
        if not self.surfaces:
            self.set_surfaces()
        return self.surfaces

    def count(self):
        return len(self.surfaces)

    def get_random_surface(self):
        random_ws = self.surfaces[
            random.randint(0, self.count - 1)]
        return random_ws.copy()

    def pop_surface(self):
        return self.surfaces.pop()

    def add_moving_surfaces(self):
        ws = self.pop_surface()
        self.moving_surfaces.append(ws)
        self.frame_counter = 0

    def save(self, _copy):
        _copy['0x0'] = [s.word for s in self.surfaces]
        _copy['0x1'] = [(ms.word, ms.dest) for ms in self.moving_surfaces]
        return _copy

    def load(self, _copy):
        for w in _copy['0x0']:
            self.surfaces.append(WordSurface(self.pm, self, w))
        for w, d in _copy['0x1']:
            self.moving_surfaces.append(WordSurface(self.pm, self, w, d))

    def blit(self):
        if len(self.surfaces) > 0:
            if len(self.moving_surfaces) < 1:
                self.add_moving_surfaces()
            if self.frame_counter >= self.interval:
                self.add_moving_surfaces()

        for w in self.moving_surfaces:
            if w.intercepted:
                if w.intercept_frame_counter >= self.intercept_interval:
                    self.moving_surfaces.remove(w)
                self.pm.wave.draw(w.intercept_frame_counter)
                w.surface = w.font.render(
                    w.word, False,
                    self.intercepted_color)
                w.blit()
                w.circle()
                w.draw_laser_line()
                w.intercept_frame_counter += 1
                continue

            if w.intercept(self.pm._input):
                self.pm._input = ''
                self.pm.input_surface._update()
                self.pm.win_count += 1
                w.blit()
                continue

            if w.arrived():
                if self.pm.wall_surface.flicker() < 1:
                    self.moving_surfaces.remove(w)
                    self.pm.lose_count += 1
                    continue

            w.add_dest((0, self.moving_speed), blit=True)

        self.frame_counter += 1


class InfoSurface():
    def __init__(self, pm):
        self.pm = pm
        self.ps = pm.ps
        self.surface = self.ps.surface
        self.game_info_dest = (10, 10)
        self.game_info = name_t + \
            '/' + difficulties[self.ps.difficulty_index]
        self.game_info_color = (255, 0, 255, 10)
        self.font_size = 25
        self.font = get_default_font(self.font_size)

        self.score_font_size = 66
        self.score_font = get_default_font(self.score_font_size)

        self.datetime_diff_font_size = 50
        self.datetime_diff_font = get_default_font(
            self.datetime_diff_font_size)
        self.datetime_diff_font_color = ...

        self.font = get_default_font(self.font_size)

        self.game_info_surface = self.font.render(
            self.game_info, False, self.game_info_color)

        self.score = 0
        self._pass = False
        self.win_info_surface = None

        self.score_surface = None
        self.datetime_diff_surface = None
        self.greeting_surface = None

        self.end_time = self.ps.end_time = None

    def get_score_font_color(self):
        return (20, 255, 0) if self._pass else (255, 20, 0)

    def get_win_info(self):
        return _('win: ') + str(self.pm.win_count) + '|' + _('lose: ') \
            + str(self.pm.lose_count) + '|' + _('remain: ') \
            + str(self.pm.wordsurfaces_manager.count()) + '|' \
            + _('total: ') + str(self.pm.word_count)

    def get_win_info_dest(self):
        _w, _ = self.win_info_surface.get_size()
        return [self.ps.w_width - _w, 0]

    def get_datetime_diff_str(self):
        if self.end_time is None:
            self.end_time = self.ps.end_time = datetime.now()
        diff = (self.end_time - self.pm.start_time) + self.pm.last_timedelta
        _h, _rem = divmod(diff.seconds, 3600)
        _min, _sec = divmod(_rem, 60)
        return _('Cost: ') + f'{_h}:{_min}:{_sec}'

    def blit(self):
        self.win_info_surface = self.font.render(
            self.get_win_info(), False, self.game_info_color)
        self.surface.blit(self.game_info_surface, self.game_info_dest)
        self.surface.blit(self.win_info_surface, self.get_win_info_dest())

    def get_score(self):
        self.score = int(100 * self.pm.win_count / self.pm.word_count)
        return self.score

    def get_score_pass(self):
        self._pass = self.score > 60
        return self._pass

    def get_greeting(self):
        return _('Success!') if self._pass \
            else _('Practice makes perfect, keep trying!')

    def get_score_str(self):
        return _('Score: ') + str(self.score)

    def get_greeting_dest(self):
        _w, _h = self.greeting_surface.get_size()
        _, _s_h = self.score_surface.get_size()
        return [
            self.ps.w_width_of_2 - _w / 2,
            self.ps.w_height_of_2 - _h - _s_h
        ]

    def get_score_surface_dest(self):
        _w, _h = self.score_surface.get_size()
        return [
            self.ps.w_width_of_2 - _w / 2,
            self.ps.w_height_of_2 - _h
        ]

    def get_datetime_diff_surface_dest(self):
        _w, _h = self.datetime_diff_surface.get_size()
        return [
            self.ps.w_width_of_2 - _w / 2,
            self.ps.w_height_of_2 + _h
        ]

    def score_blit(self):
        self.score = self.get_score()
        self.get_score_pass()

        self.greeting_surface = self.score_font.render(
            self.get_greeting(),
            False,
            self.get_score_font_color()
        )

        self.score_surface = self.score_font.render(
            self.get_score_str(),
            False,
            self.get_score_font_color())

        self.datetime_diff_surface = self.datetime_diff_font.render(
            self.get_datetime_diff_str(),
            False,
            self.get_score_font_color())

        self.surface.blit(
            self.greeting_surface,
            self.get_greeting_dest())

        self.surface.blit(
            self.score_surface,
            self.get_score_surface_dest())

        self.surface.blit(
            self.datetime_diff_surface,
            self.get_datetime_diff_surface_dest())


class WordSurface():
    def __init__(self, pm, _manager, word, dest=None):
        self.pm = pm
        self.ps = self.pm.ps
        self.manager = _manager
        self.wall_surface = None
        self.word = word
        self.font_color = (200, 22, 98)
        self.font = self.manager.font
        self.circle_color = (100, 20, 25, 20)
        self.circle_width = 6
        self.intercepted = False
        self.intercept_frame_counter = 0
        self.laser_color = self.manager.laser_color
        self.laser_width = self.manager.laser_width
        self.surface = self.get_surface()
        self.size = self.get_size()
        self.dest = dest if dest else self.get_random_dest()
        self.center = self.get_center()
        self.pinyins = self.get_pinyins()
        self.tip_height = None
        self.bg_color = None

    def set_tip_height(self, height=50):
        self.tip_height = height

    def get_tip_height(self):
        if not self.tip_height:
            self.set_tip_height()
        return self.tip_height

    def set_bg_color(self, color=(20, 10, 200, 100)):
        self.bg_color = color

    def get_bg_color(self):
        if not self.bg_color:
            self.set_bg_color()
        return self.bg_color

    def blit(self):
        self.draw_bg()
        self.pm.surface.blit(self.surface, self.dest)

    def set_circle_color(self, color):
        self.circle_color = color

    def set_circle_width(self, width):
        assert isinstance(width, int)
        self.circle_width = width

    def arrived(self):
        return self.get_y() + self.get_h() >= \
            self.pm.w_height - self.pm.wall_surface.h

    def get_tip_dest(self):
        return (
            self.get_x() + self.get_w() / 2,
            self.get_y() + self.get_h() + self.get_tip_height()
        )

    def get_bg_points(self):
        return [
            (self.get_x(), self.get_y()),
            (self.get_x() + self.get_w(), self.get_y()),
            (self.get_x() + self.get_w(), self.get_y() + self.get_h()),
            self.get_tip_dest(),
            (self.get_x(), self.get_y() + self.get_h())
        ]

    def draw_bg(self):
        pygame.draw.polygon(
            self.ps.surface,
            self.get_bg_color(),
            self.get_bg_points())

    def get_surface(self):
        _render = self.font.render(self.word, False, self.font_color)
        return _render

    def set_dest(self, dest):
        self.dest = dest

    def get_x(self):
        return self.dest[0]

    def get_y(self):
        return self.dest[1]

    def get_w(self):
        return self.size[0]

    def get_h(self):
        return self.size[1]

    def add_dest(self, _add, blit=False):
        if self.dest[0] < self.ps.w_width:
            self.dest[0] += _add[0]
        if self.dest[1] < self.ps.w_height:
            self.dest[1] += _add[1]
        self.center = self.get_center()
        if blit:
            self.blit()

    def set_laser_color(self, laser_color):
        self.laser_color = laser_color

    def get_laser_color():
        return self.laser_color

    def draw_laser_line(self):
        if self.wall_surface is None:
            self.wall_surface = self.pm.wall_surface
        pygame.draw.line(
            self.ps.surface, self.laser_color,
            self.wall_surface.center, self.center,
            self.laser_width)

    def get_center(self):
        return [
            self.get_x() + self.get_w() / 2,
            self.get_y() + self.get_h() / 2
        ]

    def get_circle_radius(self):
        return self.get_w() / 1.5

    def circle(self):
        pygame.draw.circle(
            self.pm.surface, self.circle_color,
            self.center, self.get_circle_radius(),
            width=self.circle_width)

    def intercept(self, _pinyin):
        for p in self.pinyins:
            self.intercepted = p in _pinyin
            if self.intercepted:
                break
        return self.intercepted

    def get_pinyins(self):
        return pinyin.get_pinyins(self.word, tone_marks='numbers')

    def get_size(self):
        return self.surface.get_size()

    def set_random_dest(self):
        self.dest = self.get_random_dest()

    def get_random_dest(self):
        return [random.randint(0, self.pm.w_width - self.get_w()), 0]

    def copy(self):
        _new = copy.copy(self)
        _new.surface = self.surface.copy()
        _new.set_random_dest()
        return _new


class PinyinMissile(GameBase):
    def __init__(self, ps):
        self.ps = ps
        # window
        self.w_width = self.ps.w_width
        self.w_height = self.ps.w_height
        self.w_height_of_2 = self.ps.w_height_of_2
        self.w_width_of_2 = self.ps.w_width_of_2
        self.w_centrex_y = self.ps.w_centrex_y
        self.running = True
        self.FPS = self.ps.FPS
        self.clock = self.ps.clock
        self._load = False
        self.subject = self.ps.subject
        self.subject_index = self.ps.subject_index
        self.subject_game_index = self.ps.subject_game_index
        self.difficulty_index = self.ps.difficulty_index
        self.main_menu = self.ps.main_menu
        self.play_menu = self.ps.play_menu
        self.save_menu = self.ps.save_menu
        self.surface = self.ps.surface
        self._input = ''
        self.font = get_default_font(45)
        self.info_surface = InfoSurface(self)
        self.wall_surface = WallSurface(self)
        self.input_surface = InputSurface(self)
        # word surface
        self.word = Word(self)
        self.words = self.word.get_words(self.difficulty_index)
        self.wordsurfaces_manager = WordSurfacesManager(self)
        self.wave = Wave(self)
        self.win_count = 0
        self.lose_count = 0
        self.word_count = len(self.words)
        self.copy_path = get_copy_path(module_str)
        self.print_game_info()
        self.last_timedelta = timedelta(0)
        self.start_time = datetime.now()
        self.end_time = None
        self._bg_img = None

    def set_bg_img(self, src_name='0x4.png'):
        self._bg_img = pygame.image.load(get_resource_path(src_name))
        self._bg_img = pygame.transform.scale(
            self._bg_img, (self.w_width, self.w_height))

    def get_bg_img(self):
        if not self._bg_img:
            self.set_bg_img()
        return self._bg_img

    def blit_bg_img(self):
        self.surface.blit(self.get_bg_img(), (0, 0))

    def print_game_info(self):
        print(self.subject.name_t, name_t, difficulties[self.difficulty_index])

    def ascii_not_symbol(self, code):
        return 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.save_menu._menu.enable()
                    self.last_timedelta += datetime.now() - self.start_time
                    self.save_menu._menu.mainloop(self.surface)
                    self.start_time = datetime.now()
                    return
                elif e.key == pygame.K_BACKSPACE:
                    self._input = self._input[0:-1]
                    self.input_surface._update()
                    return
                elif self.ascii_not_symbol(e.key):
                    self._input += pygame.key.name(e.key)
                    self.input_surface._update()
                    return

        if self.main_menu._menu.is_enabled():
            self.main_menu._menu.update(events)

        if self.play_menu._menu.is_enabled():
            self.play_menu._menu.update(events)

    def load(self):
        try:
            self._load = True
            with open(self.copy_path, 'rb') as f:
                _copy = pickle.load(f)
            self.wordsurfaces_manager.load(_copy)
            self.word_count, self.win_count, self.lose_count = _copy['0x2']
            self.last_timedelta = _copy['0x3']
            self.start()
        except e:
            print(e)

    def save(self):
        _copy = {}
        self.wordsurfaces_manager.save(_copy)
        _copy['0x2'] = (self.word_count, self.win_count, self.lose_count)
        _copy['0x3'] = (datetime.now() - self.start_time) + self.last_timedelta

        # https://docs.python.org/3/library/pickle.html?highlight=pickle
        # Warning:
        # The pickle module is not secure. Only unpickle data you trust.
        with open(self.copy_path, 'wb') as f:
            pickle.dump(_copy, f)

    def _start(self):
        if not self._load:
            self.wordsurfaces_manager.set_surfaces()

    def play(self):
        self._load = False
        self.wordsurfaces_manager.surfaces = []
        self.wordsurfaces_manager.moving_surfaces = []
        self.wordsurfaces_manager.set_surfaces()
        self.start()

    def blit_game_surface(self):
        if self.win_count + self.lose_count < self.word_count:
            self.info_surface.blit()
            self.wall_surface.blit()
            self.wordsurfaces_manager.blit()
            self.input_surface.blit()
        else:
            self.info_surface.score_blit()

    def start(self):

        self._start()

        while self.running:
            self.clock.tick(self.FPS)
            self.blit_bg_img()
            self.handle_events(pygame.event.get())
            self.blit_game_surface()
            pygame.display.update()


def enjoy(ps):
    return PinyinMissile(ps)
