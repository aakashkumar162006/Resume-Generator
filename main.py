# Markdown Resume Input Collector

print("=== Welcome to Resume Generator ===\n")

# 1. Personal Info
name = input("Full Name: ")
job_title = input("Job Title / Role: ")
email = input("Email: ")
phone = input("Phone: ")
linkedin = input("LinkedIn profile link: ")

# 2. Summary
summary = input("\nWrite a short Summary about yourself: ")

# 3. Skills
skills = []
print("\nEnter your skills (type 'done' when finished):")
while True:
    skill = input("- ")
    if skill.lower() == "done":
        break
    skills.append(skill)

# 4. Education
degree = input("\nDegree / Course: ")
institution = input("Institution: ")
grad_year = input("Year of Graduation: ")

# 5. Work Experience / Projects
projects = []
print("\nEnter your projects/work experience (type 'done' when finished):")
while True:
    title = input("Project / Role Title (or 'done'): ")
    if title.lower() == "done":
        break
    org = input("Organization / Project Name: ")
    duration = input("Duration (optional): ")
    desc = input("Short description: ")
    
    projects.append({
        "title": title,
        "org": org,
        "duration": duration,
        "desc": desc
    })

print("\nAll inputs collected successfully!")

# Generate the markdown content
resume_md = f"""# {name}

**{job_title}**

- Email: {email}
- Phone: {phone}
- LinkedIn: {linkedin}

---

## Summary

{summary}

---

## Skills

{', '.join(skills)}

---

## Education

**{degree}**, {institution} ({grad_year})

---

## Work Experience / Projects
"""

for proj in projects:
    resume_md += f"\n### {proj['title']} - {proj['org']}"
    if proj['duration']:
        resume_md += f" ({proj['duration']})"
    resume_md += f"\n{proj['desc']}\n"

# Write to Resume.md
with open("Resume.md", "w", encoding="utf-8") as f:
    f.write(resume_md)

print("\nResume.md has been generated in this folder!")

