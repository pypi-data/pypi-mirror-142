"""
Breaks a Python str into individual user=perceived "characters"
called extended grapheme clusters by implementing the Unicode UAX-29 standard, version 14.0.0
"""

from .get_property import *
from .functions import *

__all__ = ['Splinicode']

kwargs = {'CR': 0, 'LF': 1, 'Control': 2, 'Extend': 3, 'Regional_Indicator': 4, 'SpacingMark': 5,
          'L': 6, 'V': 7, 'T': 8, 'LV': 9, 'LVT': 10, 'Other': 11, 'Prepend': 12, 'E_Base': 13,
          'E_Modifier': 14, 'ZWJ': 15, 'Glue_After_Zwj': 16, 'E_Base_GAZ': 17,
          'NotBreak': 0, 'BreakStart': 1, 'Break': 2, 'BreakLastRegional': 3, 'BreakPenultimateRegional': 4,
          'Extended_Pictographic': 101}
CR = 0
LF = 1
Control = 2
Extend = 3
Regional_Indicator = 4
SpacingMark = 5
L = 6
V = 7
T = 8
LV = 9
LVT = 10
Other = 11
Prepend = 12
E_Base = 13
E_Modifier = 14
ZWJ = 15
Glue_After_Zwj = 16
E_Base_GAZ = 17

NotBreak = 0
BreakStart = 1
Break = 2
BreakLastRegional = 3
BreakPenultimateRegional = 4

Extended_Pictographic = 101


class SCHelper:
    @staticmethod
    def is_surrogate(string, index):
        return 0xd800 <= ord(string[index]) <= 0xdbff and 0xdc00 <= ord(string[index + 1]) <= 0xdfff

    @staticmethod
    def code_point_at(string, idx):
        if idx is None:
            idx = 0
        code = ord(string[idx])
        if 0xD800 <= code <= 0xDBFF and idx < len(string) - 1:
            hi = code
            low = ord(string[idx + 1])
            if 0xDC00 <= low <= 0xDFFF:
                return ((hi - 0xD800) * 0x400) + (low - 0xDC00) + 0x10000

        if 0xDC00 <= code <= 0xDFFF and idx >= 1:
            hi = ord(string[idx - 1])
            low = code
            if 0xD800 <= hi <= 0xDBFF:
                return ((hi - 0xD800) * 0x400) + (low - 0xDC00) + 0x10000
            return low
        return code

    @staticmethod
    def should_break(start, mid, end, startEmoji, midEmoji, endEmoji):
        full = [start] + mid + [end]
        fullEmoji = [startEmoji] + midEmoji + [endEmoji]
        previous = full[-2]
        previousEmoji = fullEmoji[-2]
        next = end
        nextEmoji = endEmoji

        eModifierIndex = find_last(full, E_Modifier)
        if eModifierIndex > 1 and all(c == Extend for c in full[1:eModifierIndex]) and start in [Extend, E_Base, E_Base_GAZ]:
            return Break

        rIIindex = find_last(full, Regional_Indicator)
        if rIIindex > 0 and all(e == Regional_Indicator for e in full[1:rIIindex]) and previous not in [Prepend, Regional_Indicator]:
            if len(list(filter(lambda x: x == Regional_Indicator, full))) % 2 == 1:
                return BreakLastRegional
            return BreakPenultimateRegional

        if previous == CR and next == LF:
            return NotBreak
        if previous in [Control, CR, LF]:
            if next == E_Modifier and all(c == Extend for c in mid):
                return Break
            return BreakStart
        if next in [Control, CR, LF]:
            return BreakStart
        if previous == L and next in [L, V, LV, LVT]:
            return NotBreak
        if previous in [LV, V] and next in [V, T]:
            return NotBreak
        if previous in [LVT, T] and next == T:
            return NotBreak
        if next in [Extend, ZWJ]:
            return NotBreak
        if next == SpacingMark:
            return NotBreak
        if previous == Prepend:
            return NotBreak

        previousNonExtendIndex = find_last(full, Extend) - 1 if Extend in full else len(full) - 2
        if full[previousNonExtendIndex] in [E_Base, E_Base_GAZ] and all(c == Extend for c in full[previousNonExtendIndex + 1:-1]) and next == E_Modifier:
            return NotBreak
        if previousEmoji == Extended_Pictographic and next == E_Modifier:
            return NotBreak

        previousNonExtendIndex = find_last(fullEmoji[:-1], Extended_Pictographic)
        if previousNonExtendIndex != -1 and all(e == Extend for e in full[previousNonExtendIndex + 1: -2]) and previous == ZWJ and nextEmoji == Extended_Pictographic:
            return NotBreak

        if previous == ZWJ and next in [Glue_After_Zwj, E_Base_GAZ]:
            return NotBreak

        if Regional_Indicator in mid:
            return Break
        if previous == Regional_Indicator and next == Regional_Indicator:
            return NotBreak

        return BreakStart


class Splinicode:
    def __init__(self, string):
        self.cur_grapheme = None
        self.string = string
        self.brk = None

    def next_break(self, string, index):
        if index is None:
            index = 0
        if index < 0:
            return 0
        if index >= len(string) - 1:
            return len(string)
        prevCP = SCHelper.code_point_at(string, index)
        prev = get_grapheme_break_property(prevCP, kwargs)
        prevEmoji = get_emoji_property(prevCP, kwargs)
        mid = []
        midEmoji = []
        for i in range(index + 1, len(string)):
            if SCHelper.is_surrogate(string, i - 1):
                continue

            nextCP = SCHelper.code_point_at(string, i)
            next = get_grapheme_break_property(nextCP, kwargs)
            nextEmoji = get_emoji_property(nextCP, kwargs)
            if SCHelper.should_break(prev, mid, next, prevEmoji, midEmoji, nextEmoji):
                return i

            mid.append(next)
            midEmoji.append(nextEmoji)

        return len(string)

    def split(self):
        string = self.string
        res = []
        index = 0
        brk = self.next_break(string, index)
        while brk < len(string):
            res.append(string[index:brk])
            index = brk
            brk = self.next_break(string, index)
        if index < len(string):
            res.append(string[index:])
        return res

    def __iter__(self):
        return self.cur_grapheme

    def __next__(self):
        index = 0 if self.brk is None else self.brk
        self.brk = self.next_break(self.string, index)
        if self.brk < len(self.string):
            self.cur_grapheme = self.string[index:self.brk]
            return self.cur_grapheme
        if index < len(self.string):
            self.cur_grapheme = self.string[index:]
            return self.cur_grapheme
        raise StopIteration

    def __len__(self):
        return len(self.split())

    def reverse(self):
        graphemes = self.split()
        return graphemes[::-1]
