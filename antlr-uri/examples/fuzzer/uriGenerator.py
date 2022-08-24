# Generated by Grammarinator 19.3.post100+g8a5aabf

import itertools

from math import inf
from grammarinator.runtime import *

class uriGenerator(Generator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def uri(self, parent=None):
        with RuleContext(self, UnparserRule(name='uri', parent=parent)) as current:
            self.scheme(parent=current)
            UnlexerRule(src=':', parent=current)
            self.hier_part(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    UnlexerRule(src='?', parent=current)
                    self.query(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    UnlexerRule(src='#', parent=current)
                    self.fragment_(parent=current)
            return current
    uri.min_depth = 2

    def scheme(self, parent=None):
        with RuleContext(self, UnparserRule(name='scheme', parent=parent)) as current:
            self.ALPHA(parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    choice = self._model.choice(current, 0, [0 if [1, 1, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1])])
                    if choice == 0:
                        self.ALPHA(parent=current)
                    elif choice == 1:
                        self.digit(parent=current)
                    elif choice == 2:
                        UnlexerRule(src='+', parent=current)
                    elif choice == 3:
                        UnlexerRule(src='-', parent=current)
                    elif choice == 4:
                        UnlexerRule(src='.', parent=current)
            return current
    scheme.min_depth = 1

    def hier_part(self, parent=None):
        with RuleContext(self, UnparserRule(name='hier_part', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [3, 1, 3, 1][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1])])
            if choice == 0:
                UnlexerRule(src='//', parent=current)
                self.authority(parent=current)
                self.path_abempty(parent=current)
            elif choice == 1:
                self.path_absolute(parent=current)
            elif choice == 2:
                self.path_rootless(parent=current)
            elif choice == 3:
                self.path_empty(parent=current)
            return current
    hier_part.min_depth = 1

    def authority(self, parent=None):
        with RuleContext(self, UnparserRule(name='authority', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.userinfo(parent=current)
                    UnlexerRule(src='@', parent=current)
            self.host(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    UnlexerRule(src=':', parent=current)
                    self.port(parent=current)
            return current
    authority.min_depth = 2

    def userinfo(self, parent=None):
        with RuleContext(self, UnparserRule(name='userinfo', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    choice = self._model.choice(current, 0, [0 if [1, 3, 1, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1])])
                    if choice == 0:
                        self.unreserved(parent=current)
                    elif choice == 1:
                        self.pct_encoded(parent=current)
                    elif choice == 2:
                        self.sub_delims(parent=current)
                    elif choice == 3:
                        UnlexerRule(src=':', parent=current)
            return current
    userinfo.min_depth = 0

    def host(self, parent=None):
        with RuleContext(self, UnparserRule(name='host', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [2, 3, 1][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
            if choice == 0:
                self.ip_literal(parent=current)
            elif choice == 1:
                self.ipv4address(parent=current)
            elif choice == 2:
                self.reg_name(parent=current)
            return current
    host.min_depth = 1

    def ip_literal(self, parent=None):
        with RuleContext(self, UnparserRule(name='ip_literal', parent=parent)) as current:
            UnlexerRule(src='[', parent=current)
            choice = self._model.choice(current, 0, [0 if [1, 2, 3][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
            if choice == 0:
                self.ipv6address(parent=current)
            elif choice == 1:
                self.ipv6addrz(parent=current)
            elif choice == 2:
                self.ipvfuture(parent=current)
            UnlexerRule(src=']', parent=current)
            return current
    ip_literal.min_depth = 1

    def ipv6address(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6address', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [4, 4, 4, 4, 4, 4, 4, 3, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1, 1, 1, 1, 1])])
            if choice == 0:
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.ls32(parent=current)
            elif choice == 1:
                UnlexerRule(src='::', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.ls32(parent=current)
            elif choice == 2:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 0, min=0, max=1):
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.ls32(parent=current)
            elif choice == 3:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 1, min=0, max=1):
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 2, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.ls32(parent=current)
            elif choice == 4:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 3, min=0, max=1):
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 4, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 5, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.ls32(parent=current)
            elif choice == 5:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 6, min=0, max=1):
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 7, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 8, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 9, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.ls32(parent=current)
            elif choice == 6:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 10, min=0, max=1):
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 11, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 12, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 13, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 14, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
                self.ls32(parent=current)
            elif choice == 7:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 15, min=0, max=1):
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 16, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 17, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 18, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 19, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 20, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
                self.h16(parent=current)
            elif choice == 8:
                if self._max_depth >= 3:
                    for _ in self._model.quantify(current, 21, min=0, max=1):
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 22, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 23, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 24, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 25, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 26, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        if self._max_depth >= 3:
                            for _ in self._model.quantify(current, 27, min=0, max=1):
                                self.h16(parent=current)
                                UnlexerRule(src=':', parent=current)
                        self.h16(parent=current)
                UnlexerRule(src='::', parent=current)
            return current
    ipv6address.min_depth = 0

    def ls32(self, parent=None):
        with RuleContext(self, UnparserRule(name='ls32', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [3, 3][i] > self._max_depth else w for i, w in enumerate([1, 1])])
            if choice == 0:
                self.h16(parent=current)
                UnlexerRule(src=':', parent=current)
                self.h16(parent=current)
            elif choice == 1:
                self.ipv4address(parent=current)
            return current
    ls32.min_depth = 3

    def h16(self, parent=None):
        with RuleContext(self, UnparserRule(name='h16', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [2, 2, 2, 2][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1])])
            if choice == 0:
                self.hexdig(parent=current)
            elif choice == 1:
                self.hexdig(parent=current)
                self.hexdig(parent=current)
            elif choice == 2:
                self.hexdig(parent=current)
                self.hexdig(parent=current)
                self.hexdig(parent=current)
            elif choice == 3:
                self.hexdig(parent=current)
                self.hexdig(parent=current)
                self.hexdig(parent=current)
                self.hexdig(parent=current)
            return current
    h16.min_depth = 2

    def ipv6addrz(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6addrz', parent=parent)) as current:
            self.ipv6address(parent=current)
            UnlexerRule(src='%25', parent=current)
            self.zoneid(parent=current)
            return current
    ipv6addrz.min_depth = 1

    def zoneid(self, parent=None):
        with RuleContext(self, UnparserRule(name='zoneid', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    choice = self._model.choice(current, 0, [0 if [1, 3][i] > self._max_depth else w for i, w in enumerate([1, 1])])
                    if choice == 0:
                        self.unreserved(parent=current)
                    elif choice == 1:
                        self.pct_encoded(parent=current)
            return current
    zoneid.min_depth = 0

    def ipvfuture(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipvfuture', parent=parent)) as current:
            UnlexerRule(src='v', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    self.hexdig(parent=current)
            UnlexerRule(src='.', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=1, max=inf):
                    choice = self._model.choice(current, 0, [0 if [1, 1, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
                    if choice == 0:
                        self.unreserved(parent=current)
                    elif choice == 1:
                        self.sub_delims(parent=current)
                    elif choice == 2:
                        UnlexerRule(src=':', parent=current)
            return current
    ipvfuture.min_depth = 2

    def ipv4address(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv4address', parent=parent)) as current:
            self.dec_octet(parent=current)
            UnlexerRule(src='.', parent=current)
            self.dec_octet(parent=current)
            UnlexerRule(src='.', parent=current)
            self.dec_octet(parent=current)
            UnlexerRule(src='.', parent=current)
            self.dec_octet(parent=current)
            return current
    ipv4address.min_depth = 2

    def dec_octet(self, parent=None):
        with RuleContext(self, UnparserRule(name='dec_octet', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [1, 1, 1, 1, 1][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1])])
            if choice == 0:
                self.digit(parent=current)
            elif choice == 1:
                self.digit_nz(parent=current)
                self.digit(parent=current)
            elif choice == 2:
                UnlexerRule(src='1', parent=current)
                self.digit(parent=current)
                self.digit(parent=current)
            elif choice == 3:
                UnlexerRule(src='2', parent=current)
                self.digit_lt_5(parent=current)
                self.digit(parent=current)
            elif choice == 4:
                UnlexerRule(src='25', parent=current)
                self.digit_lt_6(parent=current)
            return current
    dec_octet.min_depth = 1

    def reg_name(self, parent=None):
        with RuleContext(self, UnparserRule(name='reg_name', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    choice = self._model.choice(current, 0, [0 if [1, 3, 1][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
                    if choice == 0:
                        self.unreserved(parent=current)
                    elif choice == 1:
                        self.pct_encoded(parent=current)
                    elif choice == 2:
                        self.sub_delims(parent=current)
            return current
    reg_name.min_depth = 0

    def port(self, parent=None):
        with RuleContext(self, UnparserRule(name='port', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.digit(parent=current)
            return current
    port.min_depth = 0

    def path_abempty(self, parent=None):
        with RuleContext(self, UnparserRule(name='path_abempty', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src='/', parent=current)
                    self.segment(parent=current)
            return current
    path_abempty.min_depth = 0

    def path_absolute(self, parent=None):
        with RuleContext(self, UnparserRule(name='path_absolute', parent=parent)) as current:
            UnlexerRule(src='/', parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.segment_nz(parent=current)
                    if self._max_depth >= 1:
                        for _ in self._model.quantify(current, 1, min=0, max=inf):
                            UnlexerRule(src='/', parent=current)
                            self.segment(parent=current)
            return current
    path_absolute.min_depth = 0

    def path_rootless(self, parent=None):
        with RuleContext(self, UnparserRule(name='path_rootless', parent=parent)) as current:
            self.segment_nz(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src='/', parent=current)
                    self.segment(parent=current)
            return current
    path_rootless.min_depth = 2

    def path_empty(self, parent=None):
        with RuleContext(self, UnparserRule(name='path_empty', parent=parent)) as current:
            pass
            return current
    path_empty.min_depth = 0

    def query(self, parent=None):
        with RuleContext(self, UnparserRule(name='query', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    choice = self._model.choice(current, 0, [0 if [1, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
                    if choice == 0:
                        self.pchar(parent=current)
                    elif choice == 1:
                        UnlexerRule(src='/', parent=current)
                    elif choice == 2:
                        UnlexerRule(src='?', parent=current)
            return current
    query.min_depth = 0

    def fragment_(self, parent=None):
        with RuleContext(self, UnparserRule(name='fragment_', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    choice = self._model.choice(current, 0, [0 if [1, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
                    if choice == 0:
                        self.pchar(parent=current)
                    elif choice == 1:
                        UnlexerRule(src='/', parent=current)
                    elif choice == 2:
                        UnlexerRule(src='?', parent=current)
            return current
    fragment_.min_depth = 0

    def segment(self, parent=None):
        with RuleContext(self, UnparserRule(name='segment', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.pchar(parent=current)
            return current
    segment.min_depth = 0

    def segment_nz(self, parent=None):
        with RuleContext(self, UnparserRule(name='segment_nz', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=1, max=inf):
                    self.pchar(parent=current)
            return current
    segment_nz.min_depth = 1

    def unreserved(self, parent=None):
        with RuleContext(self, UnparserRule(name='unreserved', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [1, 1, 0, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1, 1])])
            if choice == 0:
                self.ALPHA(parent=current)
            elif choice == 1:
                self.digit(parent=current)
            elif choice == 2:
                UnlexerRule(src='-', parent=current)
            elif choice == 3:
                UnlexerRule(src='.', parent=current)
            elif choice == 4:
                UnlexerRule(src='_', parent=current)
            elif choice == 5:
                UnlexerRule(src='~', parent=current)
            return current
    unreserved.min_depth = 0

    def pchar(self, parent=None):
        with RuleContext(self, UnparserRule(name='pchar', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [1, 3, 1, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1])])
            if choice == 0:
                self.unreserved(parent=current)
            elif choice == 1:
                self.pct_encoded(parent=current)
            elif choice == 2:
                self.sub_delims(parent=current)
            elif choice == 3:
                UnlexerRule(src=':', parent=current)
            elif choice == 4:
                UnlexerRule(src='@', parent=current)
            return current
    pchar.min_depth = 0

    def pct_encoded(self, parent=None):
        with RuleContext(self, UnparserRule(name='pct_encoded', parent=parent)) as current:
            UnlexerRule(src='%', parent=current)
            self.hexdig(parent=current)
            self.hexdig(parent=current)
            return current
    pct_encoded.min_depth = 2

    def sub_delims(self, parent=None):
        with RuleContext(self, UnparserRule(name='sub_delims', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])])
            UnlexerRule(src=['!', '$', '&', "\\'", '(', ')', '*', '+', ',', ';', '='][choice], parent=current)
            return current
    sub_delims.min_depth = 0

    def digit_nz(self, parent=None):
        with RuleContext(self, UnparserRule(name='digit_nz', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [0, 0, 0, 0, 0, 0, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1, 1, 1, 1, 1])])
            UnlexerRule(src=['1', '2', '3', '4', '5', '6', '7', '8', '9'][choice], parent=current)
            return current
    digit_nz.min_depth = 0

    def digit_lt_5(self, parent=None):
        with RuleContext(self, UnparserRule(name='digit_lt_5', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [0, 0, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1])])
            UnlexerRule(src=['0', '1', '2', '3', '4'][choice], parent=current)
            return current
    digit_lt_5.min_depth = 0

    def digit_lt_6(self, parent=None):
        with RuleContext(self, UnparserRule(name='digit_lt_6', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [0, 0, 0, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1, 1])])
            UnlexerRule(src=['0', '1', '2', '3', '4', '5'][choice], parent=current)
            return current
    digit_lt_6.min_depth = 0

    def digit(self, parent=None):
        with RuleContext(self, UnparserRule(name='digit', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [0, 0, 0, 0, 0, 0, 0, 0, 0, 0][i] > self._max_depth else w for i, w in enumerate([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])])
            UnlexerRule(src=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'][choice], parent=current)
            return current
    digit.min_depth = 0

    def hexdig(self, parent=None):
        with RuleContext(self, UnparserRule(name='hexdig', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [1, 1][i] > self._max_depth else w for i, w in enumerate([1, 1])])
            if choice == 0:
                self.digit(parent=current)
            elif choice == 1:
                self.HEXALPHA(parent=current)
            return current
    hexdig.min_depth = 1

    def ALPHA(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ALPHA', parent=parent)) as current:
            choice = self._model.choice(current, 0, [0 if [0, 0, 1][i] > self._max_depth else w for i, w in enumerate([1, 1, 1])])
            if choice == 0:
                UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            elif choice == 1:
                UnlexerRule(src=self._model.charset(current, 1, self._charsets[2]), parent=current)
            elif choice == 2:
                self.HEXALPHA(parent=current)
            return current
    ALPHA.min_depth = 0

    def HEXALPHA(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEXALPHA', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[3]), parent=current)
            return current
    HEXALPHA.min_depth = 0

    _default_rule = uri

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(97, 123)])),
        2: list(itertools.chain.from_iterable([range(71, 91)])),
        3: list(itertools.chain.from_iterable([range(65, 71)])),
    }
