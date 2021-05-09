from flask import Flask, render_template,url_for,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
	with open('venv/database.txt', mode='a') as database:
		Name = data['Name']
		Email = data['email']
		Subject = data['subject']
		Message = data['message']
		file = database.write(f'\n{Name},{Email},{Subject},{Message}')


def write_to_csv(data):
	with open('venv/database.csv', newline='', mode = 'a') as database2:
		Name = data['Name']
		Email = data['email']
		Subject = data['subject']
		Message = data['message']

		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([Name,Email,Subject,Message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return render_template('thankyou.html',data = data)

	else:
		return 'something went wrong. please try again.'





# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')





# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/contact.html')
# def details():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')
