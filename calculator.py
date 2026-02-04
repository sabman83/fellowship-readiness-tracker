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
