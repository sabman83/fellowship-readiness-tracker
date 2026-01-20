from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

next_id = 6


def calculate_readiness_score(student, job_profile):
    required_skills = job_profile["required_skills"]
    student_skills = student.get("skills", [])

    # Skills score: percentage of required skills the student has
    matched_skills = [s for s in student_skills if s in required_skills]
    if required_skills:
        skills_score = len(matched_skills) / len(required_skills)  # BUG 1: missing * 100
    else:
        skills_score = 0

    # Project score: average of individual project checklist scores
    projects = student.get("projects", [])
    if projects:
        project_scores = []
        for project in projects:
            checklist = [
                project.get("has_frontend", False),
                project.get("has_backend", False),
                project.get("has_api_db", False),
                project.get("has_live_demo", False)
            ]
            score = sum(1 for item in checklist if item) / 4 * 100
            project_scores.append(score)
        avg_project_score = sum(project_scores) / len(project_scores)
    else:
        avg_project_score = 0

    # Interview average
    interview_scores = student.get("interview_scores", [])
    if interview_scores:
        interview_avg = sum(interview_scores) / len(interview_scores)
    else:
        interview_avg = 0

    # Weighted readiness score
    total = (skills_score * 0.40) + (avg_project_score * 0.35) + (interview_avg * 0.25)

    return {
        "total": round(total, 1),
        "skills": round(skills_score, 1),
        "projects": round(avg_project_score, 1),
        "interviews": round(interview_avg, 1)
    }

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


@app.route('/students/<int:student_id>')
def student_detail(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return "Student not found", 404
    return render_template('student.html')


@app.route('/api/job-profile')
def get_job_profile():
    return jsonify(JOB_PROFILE)


@app.route('/api/students', methods=['GET'])
def get_students():
    result = []
    for student in students:
        score = calculate_readiness_score(student, JOB_PROFILE)
        result.append({
            "id": student["id"],
            "name": student["name"],
            "score": score["total"],
            "skills_score": score["skills"],
            "project_score": score["projects"],
            "interview_avg": score["interviews"]
        })
    return jsonify(result)


@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    score = calculate_readiness_score(student, JOB_PROFILE)
    return jsonify({
        "id": student["id"],
        "name": student["name"],
        "skills": student["skills"],
        "projects": student["projects"],
        "interview_scores": student["interview_scores"],
        "score": score
    })


@app.route('/api/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()
    new_student = {
        "id": next_id,
        "name": data.get("student_name", ""),
        "skills": data.get("skills", []),
        "projects": data.get("projects", []),
        "interview_scores": data.get("interview_scores", [])
    }
    students.append(new_student)
    next_id += 1
    return jsonify({"id": new_student["id"], "message": "Student added"}), 201


@app.route('/api/students/<int:student_id>/interview', methods=['POST'])
def add_interview_score(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    data = request.get_json()
    # BUG 2: JS sends "score" but we expect "interview_score"
    score = data.get("interview_score")
    if score is not None:
        student["interview_scores"].append(int(score))
    return jsonify({
        "message": "Interview score recorded",
        "scores": student["interview_scores"]
    })


if __name__ == '__main__':
    app.run(debug=True)
