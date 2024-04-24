﻿# SDK Pullenti Address, version 4.23, march 2024. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
from pullenti.unisharp.Utils import Utils
from pullenti.unisharp.Misc import RefOutArgWrapper

from pullenti.morph.LanguageHelper import LanguageHelper
from pullenti.morph.MorphWordForm import MorphWordForm
from pullenti.ner.Token import Token
from pullenti.ner.TextToken import TextToken
from pullenti.ner.MetaToken import MetaToken
from pullenti.morph.MorphLang import MorphLang
from pullenti.ner.core.TerminParseAttr import TerminParseAttr
from pullenti.ner.NumberToken import NumberToken
from pullenti.ner.ReferentToken import ReferentToken
from pullenti.ner.core.Termin import Termin

class TerminCollection:
    """ Словарь некоторых обозначений, терминов, сокращений. Очень полезный класс!
    Рассчитан на быстрый поиск токена или группы токенов среди большого списка терминов.
    
    Словарь
    """
    
    class CharNode:
        
        def __init__(self) -> None:
            self.children = None;
            self.termins = None;
    
    def __init__(self) -> None:
        self.termins = list()
        self.all_add_strs_normalized = False
        self.synonyms = None
        self.tag = None;
        self.__m_root = TerminCollection.CharNode()
        self.__m_root_ua = TerminCollection.CharNode()
        self.__m_hash1 = dict()
        self.__m_hash_canonic = None
    
    def add(self, term : 'Termin') -> None:
        """ Добавить термин. После добавления нельзя вносить изменения в термин,
        кроме как в значения Tag и Tag2 (иначе потом нужно вызвать Reindex).
        
        Args:
            term(Termin): термин
        """
        if (term.acronym_can_be_smart and term.acronym_smart is None): 
            term.acronym_smart = term.acronym
        self.termins.append(term)
        self.__m_hash_canonic = (None)
        self.reindex(term)
    
    def add_string(self, termins_ : str, tag_ : object=None, lang : 'MorphLang'=None, is_normal_text : bool=False) -> 'Termin':
        """ Добавить строку в качестве записи словаря (термина).
        
        Args:
            termins_(str): строка, которая подвергается морфологическому анализу, и в термин добавляются все варианты разбора
            tag_(object): это просто значения Tag для термина
            lang(MorphLang): язык (можно null, если язык анализируемого текста)
            is_normal_text(bool): если true, то исходный текст не нужно морфологически разбирать - он уже в нормальной форме и верхнем регистре
        
        Returns:
            Termin: добавленный термин
        """
        t = Termin(termins_, lang, is_normal_text or self.all_add_strs_normalized)
        t.tag = tag_
        if (tag_ is not None and len(t.terms) == 1): 
            pass
        self.add(t)
        return t
    
    def __get_root(self, lang : 'MorphLang', is_lat : bool) -> 'CharNode':
        if (lang is not None and lang.is_ua and not lang.is_ru): 
            return self.__m_root_ua
        return self.__m_root
    
    def reindex(self, t : 'Termin') -> None:
        """ Переиндексировать термин (если после добавления у него что-либо поменялось)
        
        Args:
            t(Termin): термин для переиндексации
        """
        if (t is None): 
            return
        if (len(t.terms) > 20): 
            pass
        if (t.acronym_smart is not None): 
            self.__add_to_hash1(ord(t.acronym_smart[0]), t)
        if (t.abridges is not None): 
            for a in t.abridges: 
                if (len(a.parts[0].value) == 1): 
                    self.__add_to_hash1(ord(a.parts[0].value[0]), t)
        for v in t._get_hash_variants(): 
            self.__add_to_tree(v, t)
        if (t.additional_vars is not None): 
            for av in t.additional_vars: 
                av.ignore_terms_order = t.ignore_terms_order
                for v in av._get_hash_variants(): 
                    self.__add_to_tree(v, t)
    
    def remove(self, t : 'Termin') -> None:
        for v in t._get_hash_variants(): 
            self.__remove_from_tree(v, t)
        for li in self.__m_hash1.values(): 
            for tt in li: 
                if (tt == t): 
                    li.remove(tt)
                    break
        i = Utils.indexOfList(self.termins, t, 0)
        if (i >= 0): 
            del self.termins[i]
    
    def __add_to_tree(self, key : str, t : 'Termin') -> None:
        if (key is None): 
            return
        nod = self.__get_root(t.lang, t.lang.is_undefined and LanguageHelper.is_latin(key))
        i = 0
        while i < len(key): 
            ch = ord(key[i])
            if (nod.children is None): 
                nod.children = dict()
            nn = None
            wrapnn954 = RefOutArgWrapper(None)
            inoutres955 = Utils.tryGetValue(nod.children, ch, wrapnn954)
            nn = wrapnn954.value
            if (not inoutres955): 
                nn = TerminCollection.CharNode()
                nod.children[ch] = nn
            nod = nn
            i += 1
        if (nod.termins is None): 
            nod.termins = list()
        if (not t in nod.termins): 
            nod.termins.append(t)
    
    def __remove_from_tree(self, key : str, t : 'Termin') -> None:
        if (key is None): 
            return
        nod = self.__get_root(t.lang, t.lang.is_undefined and LanguageHelper.is_latin(key))
        i = 0
        while i < len(key): 
            ch = ord(key[i])
            if (nod.children is None): 
                return
            nn = None
            wrapnn956 = RefOutArgWrapper(None)
            inoutres957 = Utils.tryGetValue(nod.children, ch, wrapnn956)
            nn = wrapnn956.value
            if (not inoutres957): 
                return
            nod = nn
            i += 1
        if (nod.termins is None): 
            return
        if (t in nod.termins): 
            nod.termins.remove(t)
    
    def __find_in_tree(self, key : str, lang : 'MorphLang') -> typing.List['Termin']:
        if (key is None): 
            return None
        nod = self.__get_root(lang, ((lang is None or lang.is_undefined)) and LanguageHelper.is_latin(key))
        i = 0
        while i < len(key): 
            ch = ord(key[i])
            nn = None
            if (nod.children is not None): 
                wrapnn958 = RefOutArgWrapper(None)
                Utils.tryGetValue(nod.children, ch, wrapnn958)
                nn = wrapnn958.value
            if (nn is None): 
                if (ch == (32)): 
                    if (nod.termins is not None): 
                        pp = Utils.splitString(key, ' ', False)
                        res = None
                        for t in nod.termins: 
                            if (len(t.terms) == len(pp)): 
                                k = 0
                                k = 1
                                while k < len(pp): 
                                    if (not pp[k] in t.terms[k].variants): 
                                        break
                                    k += 1
                                if (k >= len(pp)): 
                                    if (res is None): 
                                        res = list()
                                    res.append(t)
                        return res
                return None
            nod = nn
            i += 1
        if (nod.termins is None or len(nod.termins) == 0): 
            return None
        return nod.termins
    
    def __add_to_hash1(self, key : int, t : 'Termin') -> None:
        li = None
        wrapli959 = RefOutArgWrapper(None)
        inoutres960 = Utils.tryGetValue(self.__m_hash1, key, wrapli959)
        li = wrapli959.value
        if (not inoutres960): 
            li = list()
            self.__m_hash1[key] = li
        if (not t in li): 
            li.append(t)
    
    def find(self, key : str) -> 'Termin':
        if (Utils.isNullOrEmpty(key)): 
            return None
        li = [ ]
        if (LanguageHelper.is_latin_char(key[0])): 
            li = self.__find_in_tree(key, MorphLang.EN)
        else: 
            li = self.__find_in_tree(key, MorphLang.RU)
            if (li is None): 
                li = self.__find_in_tree(key, MorphLang.UA)
        return (li[0] if li is not None and len(li) > 0 else None)
    
    def try_parse(self, token : 'Token', attrs : 'TerminParseAttr'=TerminParseAttr.NO) -> 'TerminToken':
        """ Попытка найти термин в словаре для начального токена
        
        Args:
            token(Token): начальный токен
            attrs(TerminParseAttr): атрибуты выделения
        
        Returns:
            TerminToken: результирующий токен, если привязалось несколько, то первый, если ни одного, то null
        
        """
        if (len(self.termins) == 0): 
            return None
        li = self.try_parse_all(token, attrs)
        if (li is not None): 
            return li[0]
        else: 
            return None
    
    def try_parse_all(self, token : 'Token', attrs : 'TerminParseAttr'=TerminParseAttr.NO) -> typing.List['TerminToken']:
        """ Попытка привязать все возможные термины
        
        Args:
            token(Token): начальный токен
            attrs(TerminParseAttr): атрибуты выделения
        
        Returns:
            typing.List[TerminToken]: список из всех подходящих привязок TerminToken или null
        
        """
        if (token is None): 
            return None
        re = self.__try_attach_all_(token, attrs, False)
        if (re is None and token.morph.language.is_ua): 
            re = self.__try_attach_all_(token, attrs, True)
        if (re is None and self.synonyms is not None): 
            re0 = self.synonyms.try_parse(token, TerminParseAttr.NO)
            if (re0 is not None and (isinstance(re0.termin.tag, list))): 
                term = self.find(re0.termin.canonic_text)
                for syn in Utils.asObjectOrNull(re0.termin.tag, list): 
                    if (term is not None): 
                        break
                    term = self.find(syn)
                if (term is not None): 
                    re0.termin = term
                    res1 = list()
                    res1.append(re0)
                    return res1
        return re
    
    def try_parse_all_sim(self, token : 'Token', simd : float) -> typing.List['TerminToken']:
        # Привязка с точностью до похожести
        # simD - параметр "похожесть (0.05..1)"
        if (simd >= 1 or (simd < 0.05)): 
            return self.try_parse_all(token, TerminParseAttr.NO)
        if (len(self.termins) == 0 or token is None): 
            return None
        tt = Utils.asObjectOrNull(token, TextToken)
        if (tt is None and (isinstance(token, ReferentToken))): 
            tt = (Utils.asObjectOrNull(token.begin_token, TextToken))
        res = None
        for t in self.termins: 
            if (not t.lang.is_undefined): 
                if (not token.morph.language.is_undefined): 
                    if (((token.morph.language) & t.lang).is_undefined): 
                        continue
            ar = t.try_parse_sim(tt, simd, TerminParseAttr.NO)
            if (ar is None): 
                continue
            ar.termin = t
            if (res is None or ar.tokens_count > res[0].tokens_count): 
                res = list()
                res.append(ar)
            elif (ar.tokens_count == res[0].tokens_count): 
                res.append(ar)
        return res
    
    def __try_attach_all_(self, token : 'Token', pars : 'TerminParseAttr'=TerminParseAttr.NO, main_root : bool=False) -> typing.List['TerminToken']:
        if (len(self.termins) == 0 or token is None): 
            return None
        s = None
        tt = Utils.asObjectOrNull(token, TextToken)
        if (tt is None and (isinstance(token, MetaToken))): 
            tt = (Utils.asObjectOrNull(token.begin_token, TextToken))
        res = None
        was_vars = False
        root = (self.__m_root if main_root else self.__get_root(token.morph.language, token.chars.is_latin_letter))
        if (tt is not None): 
            s = tt.term
            nod = root
            no_vars = False
            len0 = 0
            if ((((pars) & (TerminParseAttr.TERMONLY))) != (TerminParseAttr.NO)): 
                pass
            elif (tt.invariant_prefix_length_of_morph_vars <= len(s)): 
                len0 = (tt.invariant_prefix_length_of_morph_vars)
                i = 0
                while i < tt.invariant_prefix_length_of_morph_vars: 
                    ch = ord(s[i])
                    if (nod.children is None): 
                        no_vars = True
                        break
                    nn = None
                    wrapnn961 = RefOutArgWrapper(None)
                    inoutres962 = Utils.tryGetValue(nod.children, ch, wrapnn961)
                    nn = wrapnn961.value
                    if (not inoutres962): 
                        no_vars = True
                        break
                    nod = nn
                    i += 1
                if ((no_vars and tt.term0 is not None and tt.term != tt.term0) and tt.invariant_prefix_length_of_morph_vars <= len(tt.term0)): 
                    nod = root
                    s = tt.term0
                    no_vars = False
                    i = 0
                    while i < tt.invariant_prefix_length_of_morph_vars: 
                        ch = ord(s[i])
                        if (nod.children is None): 
                            no_vars = True
                            break
                        nn = None
                        wrapnn963 = RefOutArgWrapper(None)
                        inoutres964 = Utils.tryGetValue(nod.children, ch, wrapnn963)
                        nn = wrapnn963.value
                        if (not inoutres964): 
                            no_vars = True
                            break
                        nod = nn
                        i += 1
            if (not no_vars): 
                wrapres969 = RefOutArgWrapper(res)
                inoutres970 = self.__manage_var(token, pars, s, nod, len0, wrapres969)
                res = wrapres969.value
                if (inoutres970): 
                    was_vars = True
                i = 0
                first_pass3297 = True
                while True:
                    if first_pass3297: first_pass3297 = False
                    else: i += 1
                    if (not (i < tt.morph.items_count)): break
                    if ((((pars) & (TerminParseAttr.TERMONLY))) != (TerminParseAttr.NO)): 
                        continue
                    wf = Utils.asObjectOrNull(tt.morph.get_indexer_item(i), MorphWordForm)
                    if (wf is None): 
                        continue
                    if ((((pars) & (TerminParseAttr.INDICTIONARYONLY))) != (TerminParseAttr.NO)): 
                        if (not wf.is_in_dictionary): 
                            continue
                    j = 0
                    ok = True
                    if (wf.normal_case is None or wf.normal_case == s): 
                        ok = False
                    else: 
                        j = 0
                        while j < i: 
                            wf2 = Utils.asObjectOrNull(tt.morph.get_indexer_item(j), MorphWordForm)
                            if (wf2 is not None): 
                                if (wf2.normal_case == wf.normal_case or wf2.normal_full == wf.normal_case): 
                                    break
                            j += 1
                        if (j < i): 
                            ok = False
                    if (ok): 
                        wrapres965 = RefOutArgWrapper(res)
                        inoutres966 = self.__manage_var(token, pars, wf.normal_case, nod, tt.invariant_prefix_length_of_morph_vars, wrapres965)
                        res = wrapres965.value
                        if (inoutres966): 
                            was_vars = True
                    if (wf.normal_full is None or wf.normal_full == wf.normal_case or wf.normal_full == s): 
                        continue
                    j = 0
                    while j < i: 
                        wf2 = Utils.asObjectOrNull(tt.morph.get_indexer_item(j), MorphWordForm)
                        if (wf2 is not None and wf2.normal_full == wf.normal_full): 
                            break
                        j += 1
                    if (j < i): 
                        continue
                    wrapres967 = RefOutArgWrapper(res)
                    inoutres968 = self.__manage_var(token, pars, wf.normal_full, nod, tt.invariant_prefix_length_of_morph_vars, wrapres967)
                    res = wrapres967.value
                    if (inoutres968): 
                        was_vars = True
        elif (isinstance(token, NumberToken)): 
            wrapres971 = RefOutArgWrapper(res)
            inoutres972 = self.__manage_var(token, pars, str(token.value), root, 0, wrapres971)
            res = wrapres971.value
            if (inoutres972): 
                was_vars = True
        else: 
            return None
        if (not was_vars and s is not None and len(s) == 1): 
            vars0_ = [ ]
            wrapvars973 = RefOutArgWrapper(None)
            inoutres974 = Utils.tryGetValue(self.__m_hash1, ord(s[0]), wrapvars973)
            vars0_ = wrapvars973.value
            if (inoutres974): 
                for t in vars0_: 
                    if (not t.lang.is_undefined): 
                        if (not token.morph.language.is_undefined): 
                            if (((token.morph.language) & t.lang).is_undefined): 
                                continue
                    ar = t.try_parse(tt, TerminParseAttr.NO)
                    if (ar is None): 
                        continue
                    ar.termin = t
                    if (res is None): 
                        res = list()
                        res.append(ar)
                    elif (ar.tokens_count > res[0].tokens_count): 
                        res.clear()
                        res.append(ar)
                    elif (ar.tokens_count == res[0].tokens_count): 
                        res.append(ar)
        if (res is not None): 
            ii = 0
            max0_ = 0
            i = 0
            while i < len(res): 
                if (res[i].length_char > max0_): 
                    max0_ = res[i].length_char
                    ii = i
                i += 1
            if (ii > 0): 
                v = res[ii]
                del res[ii]
                res.insert(0, v)
        return res
    
    def __manage_var(self, token : 'Token', pars : 'TerminParseAttr', v : str, nod : 'CharNode', i0 : int, res : typing.List['TerminToken']) -> bool:
        i = i0
        while i < len(v): 
            ch = ord(v[i])
            if (nod.children is None): 
                return False
            nn = None
            wrapnn975 = RefOutArgWrapper(None)
            inoutres976 = Utils.tryGetValue(nod.children, ch, wrapnn975)
            nn = wrapnn975.value
            if (not inoutres976): 
                return False
            nod = nn
            i += 1
        vars0_ = nod.termins
        if (vars0_ is None or len(vars0_) == 0): 
            return False
        for t in vars0_: 
            ar = t.try_parse(token, pars)
            if (ar is not None): 
                ar.termin = t
                if (res.value is None): 
                    res.value = list()
                    res.value.append(ar)
                elif (ar.tokens_count > res.value[0].tokens_count): 
                    res.value.clear()
                    res.value.append(ar)
                elif (ar.tokens_count == res.value[0].tokens_count): 
                    j = 0
                    j = 0
                    while j < len(res.value): 
                        if (res.value[j].termin == ar.termin): 
                            break
                        j += 1
                    if (j >= len(res.value)): 
                        res.value.append(ar)
            if (t.additional_vars is not None): 
                for av in t.additional_vars: 
                    ar = av.try_parse(token, pars)
                    if (ar is None): 
                        continue
                    ar.termin = t
                    if (res.value is None): 
                        res.value = list()
                        res.value.append(ar)
                    elif (ar.tokens_count > res.value[0].tokens_count): 
                        res.value.clear()
                        res.value.append(ar)
                    elif (ar.tokens_count == res.value[0].tokens_count): 
                        j = 0
                        j = 0
                        while j < len(res.value): 
                            if (res.value[j].termin == ar.termin): 
                                break
                            j += 1
                        if (j >= len(res.value)): 
                            res.value.append(ar)
        return len(v) > 1
    
    def find_termins_by_termin(self, termin : 'Termin') -> typing.List['Termin']:
        """ Поискать эквивалентные термины
        
        Args:
            termin(Termin): термин
        
        Returns:
            typing.List[Termin]: список эквивалентных терминов Termin или null
        """
        res = None
        for v in termin._get_hash_variants(): 
            vars0_ = self.__find_in_tree(v, termin.lang)
            if (vars0_ is None): 
                continue
            for t in vars0_: 
                if (t.is_equal(termin)): 
                    if (res is None): 
                        res = list()
                    if (not t in res): 
                        res.append(t)
        return res
    
    def find_termins_by_string(self, str0_ : str, lang : 'MorphLang'=None) -> typing.List['Termin']:
        """ Поискать термины по строке
        
        Args:
            str0_(str): поисковая строка
            lang(MorphLang): возможный язык (null)
        
        Returns:
            typing.List[Termin]: список терминов Termin или null
        """
        return self.__find_in_tree(str0_, lang)
    
    def find_termins_by_canonic_text(self, text : str) -> typing.List['Termin']:
        if (self.__m_hash_canonic is None): 
            self.__m_hash_canonic = dict()
            for t in self.termins: 
                ct = t.canonic_text
                li = [ ]
                wrapli977 = RefOutArgWrapper(None)
                inoutres978 = Utils.tryGetValue(self.__m_hash_canonic, ct, wrapli977)
                li = wrapli977.value
                if (not inoutres978): 
                    li = list()
                    self.__m_hash_canonic[ct] = li
                if (not t in li): 
                    li.append(t)
        res = [ ]
        wrapres979 = RefOutArgWrapper(None)
        inoutres980 = Utils.tryGetValue(self.__m_hash_canonic, text, wrapres979)
        res = wrapres979.value
        if (not inoutres980): 
            return None
        else: 
            return res