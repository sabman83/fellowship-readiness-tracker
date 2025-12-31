let jobProfile = null;

async function loadJobProfile() {
    const res = await fetch('/api/job-profile');
    jobProfile = await res.json();

    const container = document.getElementById('job-profile-content');
    container.innerHTML = `
        <div class="job-header">
            <div>
                <h3>${jobProfile.title}</h3>
                <p class="company">${jobProfile.company}</p>
            </div>
        </div>
        <p class="job-description">${jobProfile.description}</p>
        <div class="skills-required">
            <strong>Required Skills:</strong>
            <div class="skill-badges">
                ${jobProfile.required_skills.map(s => `<span class="badge">${s}</span>`).join('')}
            </div>
        </div>
    `;

    // Populate skills checkboxes in the add-student modal
    const checkboxContainer = document.getElementById('skills-checkboxes');
    checkboxContainer.innerHTML = jobProfile.required_skills.map(skill => `
        <label class="checkbox-label">
            <input type="checkbox" name="skill" value="${skill}">
            ${skill}
        </label>
    `).join('');
}

async function loadStudents() {
    const res = await fetch('/api/students');
    const students = await res.json();

    const tbody = document.getElementById('students-tbody');
    if (!students.length) {
        tbody.innerHTML = '<tr><td colspan="6">No fellows added yet.</td></tr>';
        return;
    }

    tbody.innerHTML = students.map(s => {
        return `
            <tr>
                <td><strong>${s.name}</strong></td>
                <td>--</td>
                <td>--</td>
                <td>--</td>
                <td>--</td>
                <td><a href="/students/${s.id}" class="btn btn-sm">View</a></td>
            </tr>
        `;
    }).join('');
}

function openAddStudentModal() {
    document.getElementById('add-student-modal').classList.remove('hidden');
}

function closeAddStudentModal() {
    document.getElementById('add-student-modal').classList.add('hidden');
    document.getElementById('add-student-form').reset();
}

document.getElementById('add-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('student-name').value.trim();
    const selectedSkills = Array.from(
        document.querySelectorAll('#skills-checkboxes input[type="checkbox"]:checked')
    ).map(cb => cb.value);

    const projectName = document.getElementById('project-name').value.trim();
    const projects = [];
    if (projectName) {
        projects.push({
            name: projectName,
            has_frontend: document.getElementById('proj-frontend').checked,
            has_backend: document.getElementById('proj-backend').checked,
            has_api_db: document.getElementById('proj-api-db').checked,
            has_live_demo: document.getElementById('proj-live-demo').checked
        });
    }

    const i1 = parseInt(document.getElementById('interview-1').value) || 0;
    const i2 = parseInt(document.getElementById('interview-2').value) || 0;
    const i3 = parseInt(document.getElementById('interview-3').value) || 0;

    const payload = {
        student_name: name,
        skills: selectedSkills,
        projects: projects,
        interview_scores: [i1, i2, i3].filter(s => s > 0)
    };

    const res = await fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    if (res.ok) {
        closeAddStudentModal();
        await loadStudents();
    }
});

// Initialize
loadJobProfile();
loadStudents();
