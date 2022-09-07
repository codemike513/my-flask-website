from flask import Flask, render_template, jsonify

app = Flask(__name__)

COURSES = [
    {
        'id': 1,
        'title': 'Python Beginner to Pro',
        'price': 'Rs. 2200'
    },
    {
        'id': 2,
        'title': 'Hands-On Machine Learning',
        'price': 'Rs. 4000'
    },
    {
        'id': 3,
        'title': 'Blockchain',
        'price': 'Rs. 3000'
    },
    {
        'id': 4,
        'title': 'Web Development Bootcamp',
        'price': 'Rs. 3500'
    },
    {
        'id': 5,
        'title': 'Image Processing with OpenCV',
        'price': 'Rs. 3200'
    },
    {
        'id': 6,
        'title': 'Flutter with Firebase',
        'price': 'Rs. 2500'
    },
    {
        'id': 7,
        'title': 'Devops Fundamentals',
        'price': 'Rs. 3000'
    },
]


@app.route('/')
def hello():
    return render_template('home.html',
                           courses=COURSES,
                           company_name='Mike Codes')

@app.route('/course')
def course():
  return render_template('course.html')

@app.route("/api/courses")
def list_courses():
    return jsonify(COURSES)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
