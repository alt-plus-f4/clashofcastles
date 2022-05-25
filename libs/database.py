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
		self.cursor.execute(f"SELECT * FROM `userdata` WHERE `userdata`.`id` = {usrid};")
		return self.cursor.fetchall()
	
	def selectByTag(self, tag):
		self.cursor.execute(f"SELECT * FROM `userdata` WHERE `userdata`.`tag` = '{tag}';")
		return self.cursor.fetchall()
		
	def selectAll(self):
		self.cursor.execute(f"SELECT * FROM `userdata`;")
		return self.cursor.fetchall()

	def delete(self, usrid):
		self.cursor.execute(f"DELETE FROM `userdata` WHERE `usrdata`.`id` = {usrid};")
		self.db.commit()

	def insert(self, base, gold, elixir, tag):
		self.cursor.execute(f"INSERT INTO `userdata` (`id`, `base`, `gold`, `elixir`, `tag`) VALUES (NULL, '{base}', '{gold}', '{elixir}', '{tag}');")
		self.db.commit()
	
	def get_base(self, tag):
		self.cursor.execute(f"SELECT `base` FROM `userdata` WHERE `userdata`.`tag` = '{tag}';")
		return self.cursor.fetchone()[0]
	
	def get_money(self, tag):
		self.cursor.execute(f"SELECT `gold` FROM `userdata` WHERE `userdata`.`tag` = '{tag}';")
		return self.cursor.fetchone()[0]

	def get_elixir(self, tag):
		self.cursor.execute(f"SELECT `elixir` FROM `userdata` WHERE `userdata`.`tag` = '{tag}';")
		return self.cursor.fetchone()[0]
	
	def save(self, base, gold, elixir, tag):
		self.cursor.execute(f"UPDATE `userdata` SET `base` = '{base}', `gold` = '{gold}', `elixir` = '{elixir}' WHERE `userdata`.`tag` = '{tag}';")
		self.db.commit()