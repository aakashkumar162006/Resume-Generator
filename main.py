import json
import datetime
import pypandoc

print("=== Welcome to Resume Generator ===\n")

# Ask user if they want to load data from JSON
use_json = input("Load data from data.json? (y/n): ").lower() == "y"

# === Loading Data From JSON ===
if use_json:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Load data from JSON
    name = data["name"]
    job_title = data["job_title"]
    email = data["email"]
    phone = data["phone"]
    linkedin = data["linkedin"]
    summary = data["summary"]
    skills = data["skills"]
    schools = data.get("schools", {})
    degrees = data.get("degrees", [])
    projects = data.get("projects", [])
    certificates = data.get("certifications", [])

else:

    # === Manual Input Collection ===
    name = input("Full Name: ")
    job_title = input("Job Title / Role: ")
    email = input("Email: ")
    phone = input("Phone: ")
    linkedin = input("LinkedIn profile link: ")

    summary = input("\nWrite a short Summary about yourself: ")

    # Skills
    skills = []
    print("\nEnter your skills (type 'done' when finished):")
    while True:
        skill = input("- ")
        if skill.lower() == "done":
            break
        skills.append(skill)

    # Education
    degrees = []
    schools = {}
    while True:
        institute = input("\nEnter 'school', 'college', or 'done': ").lower()
        if institute == "done":
            break
        elif institute == "school":
            sslc_year = input("Year of SSLC: ")
            sslc_name = input("School Name (SSLC): ")
            hsc_year = input("Year of HSC: ")
            hsc_name = input("School Name (HSC): ")
            schools = {
                "sslc": {"year": sslc_year, "name": sslc_name},
                "hsc": {"year": hsc_year, "name": hsc_name}
            }
        elif institute == "college":
            degree = input("Degree / Course: ")
            institution = input("Institution: ")
            grad_year = input("Year of Graduation: ")
            degrees.append({
                "degree": degree,
                "institution": institution,
                "grad_year": grad_year
            })

    # Work Experience / Projects
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

    #Certifications
    certificates=[]
    while True:
        cert_name=input("Certificate / Certificate Name(type 'done' when finished): ")
        if cert_name.lower() == "done":
            break
        cert_academy=input("The Academy or Institution that provided it: ")
        certificates.append({'name':cert_name,'provider':cert_academy})

# Auto-save data to JSON only if we used manual input
if not use_json:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump({
            "name": name,
            "job_title": job_title,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "summary": summary,
            "skills": skills,
            "schools": schools,
            "degrees": degrees,
            "projects": projects,
            "certifications": certificates
        }, f, indent=4)
    print("💾 Data saved to data.json!")


print("\nAll inputs collected successfully!")

# ===== Generate Markdown =====
resume_md = f"""# Resume

#### **Job Title:** {job_title}

### Personal Info
- **Name:** {name}
- **Email:** {email}
- **Phone:** {phone}
- **LinkedIn:** [{linkedin}]({linkedin})

---

### Summary
{summary}

---

### Skills
- {"\n- ".join(skills)}

---

### Education
"""

if schools:
    resume_md += f"\n- **SSLC:** {schools['sslc']['name']} ({schools['sslc']['year']})\n"
    resume_md += f"- **HSC:** {schools['hsc']['name']} ({schools['hsc']['year']})\n"

for d in degrees:
    resume_md += f"\n- **{d['degree']}**, {d['institution']} ({d['grad_year']})\n"

resume_md += "\n---\n\n### Work Experience / Projects\n"

for proj in projects:
    resume_md += f"\n#### {proj['title']} — {proj['org']}"
    if proj['duration']:
        resume_md += f" (*{proj['duration']}*)"
    resume_md += f"\n{proj['desc']}\n"

resume_md += "\n---\n\n### Certifications\n"
for cert in certificates:
    resume_md+=f"\n\n - {cert['name']} ({cert['provider']})"



#=== Write to Resume.md ===
with open("Resume.md", "w", encoding="utf-8") as f:
    f.write(resume_md)

print("\n✅ Resume.md has been generated in this folder!")


# ===== Convert Markdown to PDF =====
try:
    pdf_name = f"Resume_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pypandoc.convert_file("Resume.md", "pdf", outputfile=pdf_name, extra_args=['--standalone'])
    print(f"✅ {pdf_name} has been generated in this folder!")

except Exception as e:
    print("⚠️ PDF generation failed:", e)
    print("Make sure Pandoc is installed and added to your system PATH.")