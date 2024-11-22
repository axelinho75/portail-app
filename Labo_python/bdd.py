import sqlite3
import hashlib

connexion = sqlite3.connect('bdd.db')
curseur = connexion.cursor()

curseur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, email TEXT, num_tel TEXT, role TEXT, droit TEXT, login TEXT, password TEXT)')

admin_mdp = hashlib.sha256('admin'.encode()).hexdigest()
curseur.execute('INSERT INTO users (nom, prenom, email, num_tel, role, droit, login, password) VALUES (?,?,?,?,?,?,?,?)', ('admin', 'admin', 'test@test.com', '0606060606', 'admin', 'admin', 'admin', admin_mdp))
connexion.commit()

connexion.close()