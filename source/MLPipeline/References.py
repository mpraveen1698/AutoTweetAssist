"""
    File Name : References.py
    File Description : References class for keeping the constants, tokens and reference path
"""

import os
import sys

class References:

    ROOT_DIR = "/Users/praveenkumar/Desktop/Fall 2024/Automatic-Tweet-Response-system-main/"
    ONE = 1
    ZERO = 0
    BATCH_SIZE_BINARY_EVALUATE = 32

    BINARY_INPUT_LEN = 21
    MAX_FEATURES_BINARY = 2000

    OUTPUT = "output-new/"
    INPUT = "input/"

    # The maximum number of words to be used. (most frequent)
    MAX_NB_WORDS = 50000
    # Max number of words in each complaint.
    MAX_SEQUENCE_LENGTH = 250
    # This is fixed. Embedding
    EMBEDDING_DIM = 100

    PIPE_EXECPTIONS = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    # Training data for NER
    TRAIN_DATA = [
        ("Walmart is a leading e-commerce company", {"entities": [(0, 7, "ORG")]}),
        ("I reached Chennai yesterday.", {"entities": [(19, 28, "GPE")]}),
        ("I recently ordered a book from Amazon", {"entities": [(24, 32, "ORG")]}),
        ("I was driving a BMW", {"entities": [(16, 19, "PRODUCT")]}),
        ("I ordered this from ShopClues", {"entities": [(20, 29, "ORG")]}),
        ("Fridge can be ordered in Amazon ", {"entities": [(0, 6, "PRODUCT")]}),
        ("I bought a new Washer", {"entities": [(16, 22, "PRODUCT")]}),
        ("I bought a old table", {"entities": [(16, 21, "PRODUCT")]}),
        ("I bought a fancy dress", {"entities": [(18, 23, "PRODUCT")]}),
        ("I rented a camera", {"entities": [(12, 18, "PRODUCT")]}),
        ("I rented a tent for our trip", {"entities": [(12, 16, "PRODUCT")]}),
        ("I rented a screwdriver from our neighbour", {"entities": [(12, 22, "PRODUCT")]}),
        ("I repaired my computer", {"entities": [(15, 23, "PRODUCT")]}),
        ("I got my clock fixed", {"entities": [(16, 21, "PRODUCT")]}),
        ("I got my truck fixed", {"entities": [(16, 21, "PRODUCT")]}),
        ("Flipkart started it's journey from zero", {"entities": [(0, 8, "ORG")]}),
        ("I recently ordered from Max", {"entities": [(24, 27, "ORG")]}),
        ("Flipkart is recognized as leader in market", {"entities": [(0, 8, "ORG")]}),
        ("Virgin America is recognized as leader in market", {"entities": [(0, 14, "ORG")]}),
        ("Virgin America is the best airline ever", {"entities": [(0, 14, "ORG")]}),
        ("I recently ordered from Swiggy", {"entities": [(24, 29, "ORG")]}),
        ("Proj_DirectedStudies is a great airline.", {"entities": [(0, 14, "ORG")]}),
        ("Proj_DirectedStudies is a great airline.", {"entities": [(0, 14, "ORG")]}),
        ("Proj_DirectedStudies is a great airline.", {"entities": [(0, 15, "ORG")]}),
        ("Proj_DirectedStudies is a great airline.", {"entities": [(0, 15, "ORG")]})
    ]

    #Insert your IP with Port 9092 Eg- "34.221.72.51:9092"
    BOOTSTRAP_SERVER = "localhost:9092"

    TOPIC_NAME = "tweet-data"

    SINK_TOPIC="sink-data"

    # PARC_PATH = "./parc_sample"

    # Insert your credentials for Tweet
    consumer_key = "excGmpgYvQTjLeMgXWHxFIczo"
    consumer_secret = "uIj0ldQKzfi7hGU3Fb6HC4vloimoB7cMWatnF2LoFZ5MswBAMy"
    access_token = "1853216357006954496-MbnigHotkFXYoKuXdBoPln9UED7BbZ"
    access_token_secret = "A1UyV3fyjUxZfQ2xLXuaIeUuoUaTPx8HYlRxlulxBCUmD"

    TRACK_TWEET = "Proj_DirectedStudies"

    # api-endpoint
    #Insert your IP with Port 5000 Eg- "http://34.221.72.51:5000/"
    URL = "http://127.0.0.1:5000"

    BEARER_TOKEN= "AAAAAAAAAAAAAAAAAAAAAD8WwwEAAAAAKqFi8rire0kRaFL%2FkfmAZteY%2BBY%3DsiPp46hvu8fktNbpyhYj3N0lOtflCV66FphbsB1HHEOo3AQfOa"
