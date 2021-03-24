from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/login')
def login_page():
	return render_template('login.html')

@app.route('/page1', methods = ['POST', 'GET'])
def page1_page():
	if request.method == 'POST':
		try:
			con = sqlite3.connect('virtual_stratup_portal4.db')
			role_id = request.form['role_id']
			user_name = request.form['user_name']
			email = request.form['email']
			password = request.form['Password']
			address = request.form['Address']
			contact = request.form['contact']

			cur = con.cursor()
			cur.execute("INSERT INTO user (Role_ID, Name, Email, Password, Address, Contact) VALUES (?,?,?,?,?,?)", (role_id, user_name, email, password, address, contact))

			con.commit()
			msg = "User successfully created."
			print(msg)
			con.close()

		except:
			con.rollback()
			con.close()
			msg = "Error in creating user."
			print(msg)

		finally:
			return render_template('page1.html', flash_message="False")
	
	else:
		return render_template('page1.html', flash_message="False")

@app.route('/welcome', methods = ['GET', 'POST'])
def welcome_page():
	if request.method == 'POST':
		try:
			con = sqlite3.connect('virtual_stratup_portal4.db')
			cursor = con.cursor()
			email = request.form['Email']
			password = request.form['Password']
			# cursor.execute("SELECT * from user WHERE (Email = ? and Password = ?)", (email, password)):
			cursor.execute("SELECT count(*) from user WHERE (Email = ? and Password = ?)", (email, password))
			user_rows = cursor.fetchall()
			no_of_users = user_rows[0][0]
			if no_of_users == 1:
				print("User exist")
				cursor.execute("SELECT Name from user WHERE (Email = ? and Password = ?)", (email, password))
				rows = cursor.fetchall()
				print(rows[0][0])
				return render_template('welcome.html', name = rows[0][0])
			else:
				print("Oops! Username or password not matched.")
				return render_template('page1.html', flash_message="True")
			# print(cursor.fetchall())

			con.close()
		except:
			con.rollback()
			con.close()
	else:
		return render_template('home.html', flash_message="False")




@app.route('/registration')
def register_page():
	return render_template('registration.html')

@app.route('/startup')
def startup_page():
	return render_template('startup.html')

if __name__ == '__main__':
   app.run(debug = True)