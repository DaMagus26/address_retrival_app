# SDK Pullenti Address, version 4.23, march 2024. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import xml.etree
import typing
from pullenti.unisharp.Utils import Utils

from pullenti.morph.MorphLang import MorphLang
from pullenti.ner.core.Termin import Termin
from pullenti.ner.org.OrgProfile import OrgProfile
from pullenti.ner.org.internal.OrgItemTypeTyp import OrgItemTypeTyp

class OrgItemTypeTermin(Termin):
    
    def __init__(self, s : str, lang_ : 'MorphLang'=None, p1 : 'OrgProfile'=OrgProfile.UNDEFINED, p2 : 'OrgProfile'=OrgProfile.UNDEFINED) -> None:
        super().__init__(s, lang_, False)
        self.__m_typ = OrgItemTypeTyp.UNDEFINED
        self.must_be_partof_name = False
        self.is_pure_prefix = False
        self.can_be_normal_dep = False
        self.can_has_number = False
        self.can_has_single_name = False
        self.can_has_latin_name = False
        self.must_has_capital_name = False
        self.is_top = False
        self.can_be_single_geo = False
        self.is_doubt_word = False
        self.coeff = 0
        self.profiles = list()
        if (p1 != OrgProfile.UNDEFINED): 
            self.profiles.append(p1)
        if (p2 != OrgProfile.UNDEFINED): 
            self.profiles.append(p2)
    
    @property
    def typ(self) -> 'OrgItemTypeTyp':
        if (self.is_pure_prefix): 
            return OrgItemTypeTyp.PREFIX
        return self.__m_typ
    @typ.setter
    def typ(self, value) -> 'OrgItemTypeTyp':
        if (value == OrgItemTypeTyp.PREFIX): 
            self.is_pure_prefix = True
            self.__m_typ = OrgItemTypeTyp.ORG
        else: 
            self.__m_typ = value
            if (self.__m_typ == OrgItemTypeTyp.DEP or self.__m_typ == OrgItemTypeTyp.DEPADD): 
                if (not OrgProfile.UNIT in self.profiles): 
                    self.profiles.append(OrgProfile.UNIT)
        return value
    
    @property
    def _profile(self) -> 'OrgProfile':
        return OrgProfile.UNDEFINED
    @_profile.setter
    def _profile(self, value) -> 'OrgProfile':
        self.profiles.append(value)
        return value
    
    def __copy_from(self, it : 'OrgItemTypeTermin') -> None:
        self.profiles.extend(it.profiles)
        self.is_pure_prefix = it.is_pure_prefix
        self.can_be_normal_dep = it.can_be_normal_dep
        self.can_has_number = it.can_has_number
        self.can_has_single_name = it.can_has_single_name
        self.can_has_latin_name = it.can_has_latin_name
        self.must_be_partof_name = it.must_be_partof_name
        self.must_has_capital_name = it.must_has_capital_name
        self.is_top = it.is_top
        self.can_be_normal_dep = it.can_be_normal_dep
        self.can_be_single_geo = it.can_be_single_geo
        self.is_doubt_word = it.is_doubt_word
        self.coeff = it.coeff
    
    @staticmethod
    def deserialize_src(xml0_ : xml.etree.ElementTree.Element, set0_ : 'OrgItemTypeTermin') -> typing.List['OrgItemTypeTermin']:
        res = list()
        is_set = Utils.getXmlLocalName(xml0_) == "set"
        if (is_set): 
            set0_ = OrgItemTypeTermin(None)
            res.append(set0_)
        if (xml0_.attrib is None): 
            return res
        for a in xml0_.attrib.items(): 
            nam = Utils.getXmlAttrLocalName(a)
            if (not nam.startswith("name")): 
                continue
            lang_ = MorphLang.RU
            if (nam == "nameUa"): 
                lang_ = MorphLang.UA
            elif (nam == "nameEn"): 
                lang_ = MorphLang.EN
            it = None
            for s in Utils.splitString(a[1], ';', False): 
                if (not Utils.isNullOrEmpty(s)): 
                    if (it is None): 
                        it = OrgItemTypeTermin(s, lang_)
                        res.append(it)
                        if (set0_ is not None): 
                            it.__copy_from(set0_)
                    else: 
                        it.add_variant(s, False)
        for a in xml0_.attrib.items(): 
            nam = Utils.getXmlAttrLocalName(a)
            if (nam.startswith("name")): 
                continue
            if (nam.startswith("abbr")): 
                lang_ = MorphLang.RU
                if (nam == "abbrUa"): 
                    lang_ = MorphLang.UA
                elif (nam == "abbrEn"): 
                    lang_ = MorphLang.EN
                for r in res: 
                    if (r.lang.equals(lang_)): 
                        r.acronym = a[1]
                continue
            if (nam == "profile"): 
                li = list()
                for s in Utils.splitString(a[1], ';', False): 
                    try: 
                        p = Utils.valToEnum(s, OrgProfile)
                        if (p != OrgProfile.UNDEFINED): 
                            li.append(p)
                    except Exception as ex: 
                        pass
                for r in res: 
                    r.profiles = li
                continue
            if (nam == "coef"): 
                v = float(a[1])
                for r in res: 
                    r.coeff = v
                continue
            if (nam == "partofname"): 
                for r in res: 
                    r.must_be_partof_name = a[1] == "true"
                continue
            if (nam == "top"): 
                for r in res: 
                    r.is_top = a[1] == "true"
                continue
            if (nam == "geo"): 
                for r in res: 
                    r.can_be_single_geo = a[1] == "true"
                continue
            if (nam == "purepref"): 
                for r in res: 
                    r.is_pure_prefix = a[1] == "true"
                continue
            if (nam == "number"): 
                for r in res: 
                    r.can_has_number = a[1] == "true"
                continue
            raise Utils.newException("Unknown Org Type Tag: " + Utils.getXmlAttrName(a), None)
        return res
    
    @staticmethod
    def _new1929(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgProfile', _arg4 : bool, _arg5 : float) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2, _arg3)
        res.can_has_latin_name = _arg4
        res.coeff = _arg5
        return res
    
    @staticmethod
    def _new1934(_arg1 : str, _arg2 : bool, _arg3 : float) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.can_has_latin_name = _arg2
        res.coeff = _arg3
        return res
    
    @staticmethod
    def _new1938(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : float, _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.coeff = _arg3
        res.can_has_latin_name = _arg4
        return res
    
    @staticmethod
    def _new1954(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgProfile', _arg4 : float, _arg5 : 'OrgItemTypeTyp', _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2, _arg3)
        res.coeff = _arg4
        res.typ = _arg5
        res.is_top = _arg6
        res.can_be_single_geo = _arg7
        return res
    
    @staticmethod
    def _new1957(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : 'OrgProfile', _arg4 : float) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res._profile = _arg3
        res.coeff = _arg4
        return res
    
    @staticmethod
    def _new1958(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : float) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res._profile = _arg4
        res.coeff = _arg5
        return res
    
    @staticmethod
    def _new1959(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : 'OrgProfile', _arg4 : float, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res._profile = _arg3
        res.coeff = _arg4
        res.can_be_single_geo = _arg5
        return res
    
    @staticmethod
    def _new1962(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res._profile = _arg4
        return res
    
    @staticmethod
    def _new1963(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res._profile = _arg4
        res.can_be_normal_dep = _arg5
        return res
    
    @staticmethod
    def _new1964(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new1965(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_be_single_geo = _arg4
        return res
    
    @staticmethod
    def _new1966(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_be_single_geo = _arg5
        return res
    
    @staticmethod
    def _new1972(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.is_top = _arg4
        res.can_be_single_geo = _arg5
        return res
    
    @staticmethod
    def _new1974(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.is_top = _arg5
        res.can_be_single_geo = _arg6
        return res
    
    @staticmethod
    def _new1975(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        return res
    
    @staticmethod
    def _new1977(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        return res
    
    @staticmethod
    def _new1980(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new1982(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_be_single_geo = _arg4
        res.can_be_normal_dep = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new1984(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_be_single_geo = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new1985(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_be_single_geo = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new1986(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_be_single_geo = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new1988(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_be_single_geo = _arg5
        res.can_has_number = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new1995(_arg1 : str, _arg2 : float, _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.acronym = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new1996(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new1997(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_number = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2000(_arg1 : str, _arg2 : float, _arg3 : 'MorphLang', _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.lang = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2009(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res._profile = _arg4
        res.can_be_single_geo = _arg5
        return res
    
    @staticmethod
    def _new2010(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.is_doubt_word = _arg4
        return res
    
    @staticmethod
    def _new2011(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.is_doubt_word = _arg5
        return res
    
    @staticmethod
    def _new2014(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        return res
    
    @staticmethod
    def _new2019(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str, _arg4 : 'OrgProfile', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        res._profile = _arg4
        res.can_be_single_geo = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2023(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res._profile = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2024(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgProfile', _arg5 : 'OrgItemTypeTyp', _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res._profile = _arg4
        res.typ = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2027(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res._profile = _arg4
        res.can_has_number = _arg5
        res.can_has_latin_name = _arg6
        return res
    
    @staticmethod
    def _new2033(_arg1 : str, _arg2 : float, _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : 'OrgProfile', _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.acronym = _arg3
        res.typ = _arg4
        res._profile = _arg5
        res.can_be_single_geo = _arg6
        res.can_has_number = _arg7
        return res
    
    @staticmethod
    def _new2034(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_be_normal_dep = _arg4
        res.can_be_single_geo = _arg5
        res.can_has_single_name = _arg6
        res.can_has_latin_name = _arg7
        res._profile = _arg8
        return res
    
    @staticmethod
    def _new2040(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2052(_arg1 : str, _arg2 : float, _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.acronym = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res.can_be_single_geo = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new2054(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile', _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_number = _arg4
        res._profile = _arg5
        res.can_has_latin_name = _arg6
        return res
    
    @staticmethod
    def _new2060(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.is_doubt_word = _arg3
        return res
    
    @staticmethod
    def _new2063(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool, _arg6 : 'OrgProfile', _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        res.can_has_latin_name = _arg7
        return res
    
    @staticmethod
    def _new2064(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : str, _arg6 : bool, _arg7 : 'OrgProfile', _arg8 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.acronym = _arg5
        res.can_has_number = _arg6
        res._profile = _arg7
        res.can_has_latin_name = _arg8
        return res
    
    @staticmethod
    def _new2065(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2079(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : str, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_number = _arg4
        res.acronym = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2080(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : str, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res.acronym = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new2081(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_number = _arg4
        return res
    
    @staticmethod
    def _new2091(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_number = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new2092(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res.can_has_latin_name = _arg6
        res.can_has_single_name = _arg7
        res._profile = _arg8
        return res
    
    @staticmethod
    def _new2095(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.is_top = _arg4
        res.can_has_single_name = _arg5
        res.can_has_latin_name = _arg6
        res.can_be_single_geo = _arg7
        res._profile = _arg8
        return res
    
    @staticmethod
    def _new2096(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.is_top = _arg5
        res.can_has_single_name = _arg6
        res.can_has_latin_name = _arg7
        res.can_be_single_geo = _arg8
        return res
    
    @staticmethod
    def _new2100(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        return res
    
    @staticmethod
    def _new2101(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2102(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2103(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2104(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new2105(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.must_be_partof_name = _arg4
        return res
    
    @staticmethod
    def _new2106(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.canonic_text = _arg4
        return res
    
    @staticmethod
    def _new2108(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.must_be_partof_name = _arg5
        return res
    
    @staticmethod
    def _new2109(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.canonic_text = _arg5
        return res
    
    @staticmethod
    def _new2115(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_number = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2116(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res.can_has_latin_name = _arg6
        res.can_has_single_name = _arg7
        return res
    
    @staticmethod
    def _new2119(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2121(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : float, _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.coeff = _arg3
        res.can_be_single_geo = _arg4
        res.can_has_single_name = _arg5
        return res
    
    @staticmethod
    def _new2122(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : float, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.typ = _arg3
        res.coeff = _arg4
        res.can_be_single_geo = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2123(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        return res
    
    @staticmethod
    def _new2124(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2126(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.is_doubt_word = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2127(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.is_doubt_word = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2128(_arg1 : str, _arg2 : float, _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.acronym = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2129(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : str, _arg5 : 'OrgItemTypeTyp', _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.acronym = _arg4
        res.typ = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2134(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2141(_arg1 : str, _arg2 : 'OrgItemTypeTyp') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        return res
    
    @staticmethod
    def _new2142(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        return res
    
    @staticmethod
    def _new2144(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.is_doubt_word = _arg4
        return res
    
    @staticmethod
    def _new2149(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.is_doubt_word = _arg3
        res.can_has_number = _arg4
        return res
    
    @staticmethod
    def _new2150(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.is_doubt_word = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2151(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : float, _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.coeff = _arg3
        res.can_has_number = _arg4
        res.can_has_single_name = _arg5
        return res
    
    @staticmethod
    def _new2153(_arg1 : str, _arg2 : str, _arg3 : 'OrgItemTypeTyp', _arg4 : float, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.acronym = _arg2
        res.typ = _arg3
        res.coeff = _arg4
        res.can_has_number = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2154(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : float, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.coeff = _arg4
        res.can_has_number = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2156(_arg1 : str, _arg2 : str, _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.acronym = _arg2
        res.typ = _arg3
        res.can_be_normal_dep = _arg4
        return res
    
    @staticmethod
    def _new2159(_arg1 : str, _arg2 : 'MorphLang', _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.acronym = _arg3
        res.typ = _arg4
        res.can_be_normal_dep = _arg5
        return res
    
    @staticmethod
    def _new2162(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_be_normal_dep = _arg3
        return res
    
    @staticmethod
    def _new2163(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_be_normal_dep = _arg4
        return res
    
    @staticmethod
    def _new2175(_arg1 : str, _arg2 : str, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.acronym = _arg2
        res.typ = _arg3
        res.can_be_normal_dep = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2176(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_be_normal_dep = _arg3
        res._profile = _arg4
        return res
    
    @staticmethod
    def _new2177(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_be_normal_dep = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2181(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_number = _arg3
        res.is_doubt_word = _arg4
        return res
    
    @staticmethod
    def _new2182(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_number = _arg3
        res.is_doubt_word = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2183(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_number = _arg4
        res.is_doubt_word = _arg5
        res.can_has_latin_name = _arg6
        res.can_has_single_name = _arg7
        return res
    
    @staticmethod
    def _new2190(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_number = _arg3
        return res
    
    @staticmethod
    def _new2191(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_number = _arg4
        return res
    
    @staticmethod
    def _new2192(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : 'OrgProfile', _arg4 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res._profile = _arg3
        res.acronym = _arg4
        return res
    
    @staticmethod
    def _new2193(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res._profile = _arg4
        res.acronym = _arg5
        return res
    
    @staticmethod
    def _new2199(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str, _arg4 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        res._profile = _arg4
        return res
    
    @staticmethod
    def _new2202(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.acronym = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2206(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res._profile = _arg3
        return res
    
    @staticmethod
    def _new2223(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        return res
    
    @staticmethod
    def _new2225(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.acronym = _arg4
        return res
    
    @staticmethod
    def _new2330(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str, _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        res.acronym_can_be_lower = _arg4
        res.can_be_single_geo = _arg5
        return res
    
    @staticmethod
    def _new2331(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str, _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        res.can_has_latin_name = _arg4
        return res
    
    @staticmethod
    def _new2334(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        res.acronym = _arg4
        return res
    
    @staticmethod
    def _new2335(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.acronym = _arg5
        return res
    
    @staticmethod
    def _new2338(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        return res
    
    @staticmethod
    def _new2343(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : str, _arg5 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        res.acronym = _arg4
        res.acronym_smart = _arg5
        return res
    
    @staticmethod
    def _new2354(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : str, _arg6 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.acronym = _arg5
        res.acronym_smart = _arg6
        return res
    
    @staticmethod
    def _new2372(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str, _arg4 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        res.acronym_smart = _arg4
        return res
    
    @staticmethod
    def _new2375(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : str, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        res.acronym = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2376(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : str, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.acronym = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2379(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        res._profile = _arg4
        return res
    
    @staticmethod
    def _new2380(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2382(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        return res
    
    @staticmethod
    def _new2386(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_latin_name = _arg5
        return res
    
    @staticmethod
    def _new2390(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool, _arg5 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        res.can_has_number = _arg4
        res.acronym = _arg5
        return res
    
    @staticmethod
    def _new2391(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_number = _arg5
        res.acronym = _arg6
        return res
    
    @staticmethod
    def _new2396(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : str, _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.acronym = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_number = _arg5
        return res
    
    @staticmethod
    def _new2410(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2411(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2412(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : 'OrgProfile', _arg4 : bool, _arg5 : float) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res._profile = _arg3
        res.can_has_latin_name = _arg4
        res.coeff = _arg5
        return res
    
    @staticmethod
    def _new2413(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_single_name = _arg4
        res.can_has_latin_name = _arg5
        return res
    
    @staticmethod
    def _new2414(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : 'OrgProfile', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res._profile = _arg4
        res.can_has_single_name = _arg5
        res.can_has_latin_name = _arg6
        return res
    
    @staticmethod
    def _new2415(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : 'OrgProfile', _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res._profile = _arg5
        res.can_has_single_name = _arg6
        res.can_has_latin_name = _arg7
        return res
    
    @staticmethod
    def _new2416(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_single_name = _arg5
        res.can_has_latin_name = _arg6
        return res
    
    @staticmethod
    def _new2417(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_single_name = _arg4
        res.can_has_latin_name = _arg5
        res.must_has_capital_name = _arg6
        return res
    
    @staticmethod
    def _new2418(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_single_name = _arg5
        res.can_has_latin_name = _arg6
        res.must_has_capital_name = _arg7
        return res
    
    @staticmethod
    def _new2421(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_be_normal_dep = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2423(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_be_normal_dep = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2424(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_single_name = _arg3
        res.can_has_latin_name = _arg4
        res.is_doubt_word = _arg5
        return res
    
    @staticmethod
    def _new2426(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_single_name = _arg4
        res.can_has_latin_name = _arg5
        res.is_doubt_word = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new2427(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool, _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_single_name = _arg3
        res.can_has_latin_name = _arg4
        res.is_doubt_word = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2428(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool, _arg5 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_single_name = _arg3
        res.can_has_latin_name = _arg4
        res._profile = _arg5
        return res
    
    @staticmethod
    def _new2429(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_single_name = _arg4
        res.can_has_latin_name = _arg5
        res.is_doubt_word = _arg6
        return res
    
    @staticmethod
    def _new2430(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : float, _arg4 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.coeff = _arg3
        res.can_has_single_name = _arg4
        return res
    
    @staticmethod
    def _new2431(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : float, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.coeff = _arg4
        res.can_has_single_name = _arg5
        return res
    
    @staticmethod
    def _new2443(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        return res
    
    @staticmethod
    def _new2444(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        return res
    
    @staticmethod
    def _new2445(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.can_be_single_geo = _arg7
        return res
    
    @staticmethod
    def _new2446(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : str, _arg6 : bool, _arg7 : bool, _arg8 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.acronym = _arg5
        res.can_has_latin_name = _arg6
        res.can_has_single_name = _arg7
        res.can_be_single_geo = _arg8
        return res
    
    @staticmethod
    def _new2453(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res.must_has_capital_name = _arg6
        return res
    
    @staticmethod
    def _new2454(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res.must_has_capital_name = _arg6
        return res
    
    @staticmethod
    def _new2455(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : float, _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.typ = _arg3
        res.coeff = _arg4
        res.can_has_latin_name = _arg5
        return res
    
    @staticmethod
    def _new2456(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgProfile', _arg4 : 'OrgItemTypeTyp', _arg5 : float, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2, _arg3)
        res.typ = _arg4
        res.coeff = _arg5
        res.can_has_latin_name = _arg6
        return res
    
    @staticmethod
    def _new2464(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgProfile', _arg4 : 'OrgItemTypeTyp', _arg5 : float, _arg6 : bool, _arg7 : str) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2, _arg3)
        res.typ = _arg4
        res.coeff = _arg5
        res.can_has_latin_name = _arg6
        res.acronym = _arg7
        return res
    
    @staticmethod
    def _new2468(_arg1 : str, _arg2 : 'OrgItemTypeTyp', _arg3 : bool, _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.typ = _arg2
        res.can_has_latin_name = _arg3
        res.can_has_single_name = _arg4
        res.must_has_capital_name = _arg5
        res.can_has_number = _arg6
        return res
    
    @staticmethod
    def _new2469(_arg1 : str, _arg2 : 'MorphLang', _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res.must_has_capital_name = _arg6
        res.can_has_number = _arg7
        return res
    
    @staticmethod
    def _new2470(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res.must_has_capital_name = _arg6
        res._profile = _arg7
        return res
    
    @staticmethod
    def _new2471(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.must_has_capital_name = _arg7
        res._profile = _arg8
        return res
    
    @staticmethod
    def _new2475(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.lang = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.must_has_capital_name = _arg7
        return res
    
    @staticmethod
    def _new2476(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : str, _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.acronym = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.must_has_capital_name = _arg7
        return res
    
    @staticmethod
    def _new2478(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res.must_has_capital_name = _arg6
        res.can_has_number = _arg7
        return res
    
    @staticmethod
    def _new2479(_arg1 : str, _arg2 : float, _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.acronym = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.must_has_capital_name = _arg7
        res.can_has_number = _arg8
        return res
    
    @staticmethod
    def _new2481(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.must_has_capital_name = _arg7
        res.can_has_number = _arg8
        return res
    
    @staticmethod
    def _new2484(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_single_name = _arg5
        res.can_be_single_geo = _arg6
        return res
    
    @staticmethod
    def _new2485(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.can_be_single_geo = _arg7
        return res
    
    @staticmethod
    def _new2493(_arg1 : str, _arg2 : float, _arg3 : str, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.acronym = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.can_has_number = _arg7
        return res
    
    @staticmethod
    def _new2494(_arg1 : str, _arg2 : str, _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool, _arg7 : bool, _arg8 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.acronym = _arg2
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        res.can_has_single_name = _arg6
        res.must_has_capital_name = _arg7
        res.can_has_number = _arg8
        return res
    
    @staticmethod
    def _new2499(_arg1 : str, _arg2 : 'MorphLang', _arg3 : float, _arg4 : 'OrgItemTypeTyp', _arg5 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1, _arg2)
        res.coeff = _arg3
        res.typ = _arg4
        res.can_has_latin_name = _arg5
        return res
    
    @staticmethod
    def _new2500(_arg1 : str, _arg2 : float, _arg3 : 'OrgItemTypeTyp', _arg4 : bool, _arg5 : bool, _arg6 : 'OrgProfile') -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.typ = _arg3
        res.can_has_latin_name = _arg4
        res.can_has_number = _arg5
        res._profile = _arg6
        return res
    
    @staticmethod
    def _new2504(_arg1 : str, _arg2 : float, _arg3 : bool, _arg4 : 'OrgItemTypeTyp', _arg5 : bool, _arg6 : bool) -> 'OrgItemTypeTermin':
        res = OrgItemTypeTermin(_arg1)
        res.coeff = _arg2
        res.can_be_normal_dep = _arg3
        res.typ = _arg4
        res.can_has_number = _arg5
        res.can_be_single_geo = _arg6
        return res