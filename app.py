from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOB_PROFILE = {
    "title": "Junior Web Developer",
    "company": "Nexus Technologies",
    "description": (
        "Nexus Technologies is seeking a Junior Web Developer to join our growing "
        "engineering team. You will build and maintain web applications, collaborate "
        "with senior developers, and contribute to both frontend and backend features. "
        "The ideal candidate has experience with modern web technologies, understands "
        "RESTful APIs, and is comfortable working with databases. This is an excellent "
        "opportunity for a recent graduate looking to launch their tech career."
    ),
    "required_skills": ["HTML", "CSS", "JavaScript", "Python", "Git", "REST APIs", "SQL", "React"]
}

students = [
    {
        "id": 1,
        "name": "Maya Patel",
        "skills": ["HTML", "CSS", "JavaScript", "Python", "Git", "SQL"],
        "projects": [
            {
                "name": "Portfolio Website",
                "has_frontend": True,
                "has_backend": False,
                "has_api_db": False,
                "has_live_demo": True
            },
            {
                "name": "Student Grade Tracker",
                "has_frontend": True,
                "has_backend": True,
                "has_api_db": True,
                "has_live_demo": False
            }
        ],
        "interview_scores": [78, 82, 79]
    },
    {
        "id": 2,
        "name": "Jordan Lee",
        "skills": ["HTML", "CSS", "JavaScript", "Git"],
        "projects": [
            {
                "name": "Landing Page",
                "has_frontend": True,
                "has_backend": False,
                "has_api_db": False,
                "has_live_demo": True
            }
        ],
        "interview_scores": [65, 70, 62]
    },
    {
        "id": 3,
        "name": "Sam Rivera",
        "skills": ["HTML", "CSS", "JavaScript", "Python", "Git", "REST APIs", "SQL", "React"],
        "projects": [
            {
                "name": "E-commerce Platform",
                "has_frontend": True,
                "has_backend": True,
                "has_api_db": True,
                "has_live_demo": True
            },
            {
                "name": "Weather Dashboard",
                "has_frontend": True,
                "has_backend": True,
                "has_api_db": False,
                "has_live_demo": True
            }
        ],
        "interview_scores": [88, 91, 85]
    },
    {
        "id": 4,
        "name": "Casey Morgan",
        "skills": ["HTML", "CSS", "JavaScript", "Python"],
        "projects": [
            {
                "name": "Task Manager",
                "has_frontend": True,
                "has_backend": True,
                "has_api_db": False,
                "has_live_demo": False
            },
            {
                "name": "Blog Platform",
                "has_frontend": True,
                "has_backend": True,
                "has_api_db": True,
                "has_live_demo": False
            }
        ],
        "interview_scores": [71, 68, 74]
    },
    {
        "id": 5,
        "name": "Taylor Kim",
        "skills": ["HTML", "CSS", "JavaScript", "Python", "Git", "REST APIs"],
        "projects": [
            {
                "name": "Recipe Finder App",
                "has_frontend": True,
                "has_backend": True,
                "has_api_db": False,
                "has_live_demo": True
            }
        ],
        "interview_scores": [75, 79, 77]
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/job-profile')
def get_job_profile():
    return jsonify(JOB_PROFILE)


@app.route('/api/students', methods=['GET'])
def get_students():
    result = []
    for student in students:
        result.append({
            "id": student["id"],
            "name": student["name"],
            "skills": student["skills"],
            "projects": student["projects"],
            "interview_scores": student["interview_scores"]
        })
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
