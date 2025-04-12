from config import *

def save(matrix = 0, gold = 0, elixir = 0, tag = ''):
    db.save(matrix, gold, elixir, tag)

def load(tag):
    tag_str = str(tag)
    return db.get_base(tag_str), db.get_money(tag_str), db.get_elixir(tag_str)