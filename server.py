from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)                  # change here to function, either txt or csv
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database - please try again'
    else:
        return 'something went wrong'
    # return render_template('login.html', error=error)


# Below can all be done with above - dynamic ranges
# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')






# @app.route('/')
# def hello_world():
#     return render_template('index_v1.html')
#
#
# @app.route('/<username>')
# def hello_user(username=''):
#     return render_template('index_v1.html', name=username)
#
#
# @app.route('/<username>/<int:post_id>')
# def user_page(username='', post_id=''):
#     return render_template('index_v1.html', name=username, post_id=post_id)
#
#
# @app.route('/about')
# def about():
#     return render_template('about_v1.html')
#
#
# @app.route('/blog')
# def blog_page():
#     return 'Testing for blog page'
#
#
# @app.route('/blog/2020/dogs')
# def blog_page2():
#     return 'Blog page about dogs'


