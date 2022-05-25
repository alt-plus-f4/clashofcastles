from config import *

def save(matrix = 0, gold = 0, elixir = 0, tag = ''):
    db.save(matrix, gold, elixir, tag)

def load(tag = ''):
    return db.get_base(tag), db.get_money(tag), db.get_elixir(tag)