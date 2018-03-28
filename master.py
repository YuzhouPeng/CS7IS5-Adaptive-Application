#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 18:42:58 2018

@author: Srubin
"""

import wiki_parser
import gensim
import pickle


def init():
    print("loading model")
    return gensim.models.KeyedVectors.load_word2vec_format('../GoogleNews-vectors-negative300.bin', binary=True)


def run_all(model, titles, topics):
    print("model loaded - parsing data")
    for title in titles:
        print("parsing data")
        all_data, content = wiki_parser.get_wiki_data(model, topics, title)
        # load into db/csv
        print("writing data")
        with open(('output-sport/' + title + '.p'), 'wb') as fp:
            pickle.dump({
                "topic": "Sports",
                "page": title,
                "data": all_data,
                "content": content}, fp, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    # get titles here
    sport = ["sport", "sports", "athletics", "running", "cricket", "football"]
    music = ["songs", "song", "music", "rock", "band", "sing"]
    # run_all(init(), ["Music", "Harmony", "Chromaticism", "Rock_music", "Alternative_rock", "Singing", "Jazz"])
    run_all(init(), ["Sport", "Cricket", "Football", "Rugby football", "Sport of athletics", "Running"], sport)
