import mysql.connector

class DataBase:
    def __init__(self, servername, username, password, dbname):
        self.servername = servername
        self.username = username
        self.password = password
        self.databasename = dbname
        self.db = None
        self.cursor = None
        self.connect()

    def connect(self):
        self.db = mysql.connector.connect(host=f"{self.servername}", user=f"{self.username}", passwd=f"{self.password}",database=f"{self.databasename}")
        self.cursor = self.db.cursor()
    
    def selectById(self, usrid):
        self.cursor.execute(f"SELECT * FROM `usrdata` WHERE `usrdata`.`id` = {usrid};")
        return self.cursor.fetchall()
    
    def selectByTag(self, tag):
        self.cursor.execute(f"SELECT * FROM `usrdata` WHERE `usrdata`.`tag` = '{tag}';")
        return self.cursor.fetchall()
        
    def selectAll(self):
        self.cursor.execute(f"SELECT * FROM `usrdata`;")
        return self.cursor.fetchall()

    def delete(self, usrid):
        self.cursor.execute(f"DELETE FROM `usrdata` WHERE `usrdata`.`id` = {usrid};")
        self.db.commit()

    def insert(self, base, gold, elixir, gems, tag):
        self.cursor.execute(f"INSERT INTO `usrdata` (`id`, `base`, `gold`, `elixir`, `gems`, `tag`) VALUES (NULL, '{base}', '{gold}', '{elixir}', '{gems}', '{tag}');")
        self.db.commit()