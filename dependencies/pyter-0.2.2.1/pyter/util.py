# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import re
import unicodedata

def preprocess_en(s):
    u"""
    記号類: 同じものは固まる、違うものは離す
    * 特殊な用法は経験ベースでくっつける
    例: e.g., a.m., p.m., etc.
    * 数字に挟まれたピリオドとカンマはくっつける
    文字 <=> a-zA-Z0-9
    記号 <=> 文字以外
    """
    s = s.rstrip()  # trail space, tab, newlineの削除
    s = re.sub(r'([^a-zA-Z0-9])(?!\1|$)', r'\1 ', s) # 前が記号で、後ろが出た文字以外
    s = re.sub(r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9])', r' \1', s) # 後ろが記号で、前が記号以外
    s = re.sub(r'\s+', ur' ', s)  # スペースの個数正規化
    s = re.sub(r'(\d) ([.,]) (\d)', ur'\1\2\3', s)  # 0 . 1 -> 0.1
    s = re.sub(r'(Dr|Jr|Prof|Rev|Gen|Mr|Mt|Mrs|Ms) .', ur'\1.', s)  # Mr . -> Mr.
    s = s.replace(u'e . g .', u'e.g.')
    s = s.replace(u'i . e .', u'e.g.')
    s = s.replace(u'U . S .', u'U.S.')
    return s

def preprocess_ja(s):
    s = s.rstrip()  # trail space, tab, newlineの削除
    s = unicodedata.normalize('NFKC', s)  # まず正規化
    return s


def preprocess(s, lang):
    funcname = 'preprocess_{0}'.format(lang)
    return globals()[funcname](s)


def split(s, lang):
    if lang == 'ja':
        return list(s)
    else:
        return s.split()


















