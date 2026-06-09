from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

docs = {
    "rmp_arnold_toffler.txt": """Source Name: Arnold Toffler Reviews
Source Type: Rate My Professors
URL or Description: Rate My Professors page for Arnold Toffler at Caldwell University

Content:
Arnold Toffler is listed as a Computer Science professor at Caldwell University. The Rate My Professors Computer Science department page lists Arnold Toffler with a quality rating of 3.5 based on 30 ratings, 60% would take again, and a 2.7 level of difficulty.

Student review notes suggest mixed experiences. Some students describe his classes as lecture-heavy, test-heavy, or based heavily on slides. Some comments mention that students need to read chapters or slides carefully to do well. Other notes describe him as accessible outside class or giving good feedback.

Useful facts for RAG:
- Professor: Arnold Toffler
- Department: Computer Science
- Quality rating: 3.5 / 5
- Ratings count: 30
- Would take again: 60%
- Difficulty: 2.7
- Common themes: lecture-heavy, test-heavy, slide-based, mixed student experience, some good feedback
- Courses mentioned in review summaries: CS195, CS196, CS225
""",

    "rmp_vladislav_veksler.txt": """Source Name: Vladislav Veksler Reviews
Source Type: Rate My Professors
URL or Description: Rate My Professors page for Vladislav Veksler at Caldwell University

Content:
Vladislav Veksler is listed as a Computer Science professor at Caldwell University. The Rate My Professors Computer Science department page lists Vladislav Veksler with a quality rating of 5.0 based on 4 ratings, 100% would take again, and a 1.3 level of difficulty.

Student review notes are very positive. Review themes include amazing lectures, being accessible outside class, giving good feedback, being inspirational, and using group projects. Student comments describe him as helpful and accessible. Several comments connect him with CS195 and CS242.

Useful facts for RAG:
- Professor: Vladislav Veksler
- Department: Computer Science
- Quality rating: 5.0 / 5
- Ratings count: 4
- Would take again: 100%
- Difficulty: 1.3
- Common themes: amazing lectures, accessible outside class, gives good feedback, inspirational, group projects
- Courses mentioned: CS195, CS242
""",

    "rmp_isaac_damoah.txt": """Source Name: Isaac Damoah Reviews
Source Type: Rate My Professors
URL or Description: Rate My Professors page for Isaac Damoah at Caldwell University

Content:
Isaac Damoah is listed on Rate My Professors for Caldwell University. The Rate My Professors Computer Science department page lists Isaac Damoah with a quality rating of 4.6 based on 19 ratings, 100% would take again, and a 2.0 level of difficulty.

Student review notes are positive. One visible review says he went out of his way to help struggling students, was always available, stayed back when students needed help, and wanted students to succeed. The review tags include clear grading criteria, gives good feedback, caring, and helpful.

Useful facts for RAG:
- Professor: Isaac Damoah
- Quality rating: 4.6 / 5
- Ratings count: 19
- Would take again: 100%
- Difficulty: 2.0
- Common themes: caring, helpful, available to students, clear grading criteria, gives good feedback
""",

    "rmp_adriana_wise.txt": """Source Name: Adriana Wise Reviews
Source Type: Rate My Professors
URL or Description: Rate My Professors page for Adriana Wise at Caldwell University

Content:
Adriana Wise is listed on Rate My Professors for Caldwell University. The visible review notes are negative. A student describes the class as difficult and says the professor read from a document for much of the semester. The review says homework due dates were unclear and exams were very difficult. The review also says the professor filled the board with equations and expected students to follow along. Attendance was taken every class.

Useful facts for RAG:
- Professor: Adriana Wise
- Common themes: difficult exams, unclear homework due dates, lecture-heavy, lots of homework, attendance required
- This source is useful for questions about difficult classes or negative student experiences.
""",

    "rmp_lowell_qually.txt": """Source Name: Lowell Qually Reviews
Source Type: Rate My Professors
URL or Description: Rate My Professors page for Lowell Qually at Caldwell University

Content:
Lowell Qually is listed on Rate My Professors for Caldwell University. The visible profile information shows 4 student ratings. One visible review for CS219 gives a quality score of 5.0 and difficulty score of 1.0. The student describes him as a great teacher, says they had him for multiple classes, and says he tries to help students understand the material. The student highly recommends him.

Useful facts for RAG:
- Professor: Lowell Qually
- Ratings count visible: 4
- Course mentioned: CS219
- Common themes: helpful, great teacher, helps students understand, highly recommended, low difficulty in visible review
""",

    "rmp_caldwell_cs_department.txt": """Source Name: Caldwell University Computer Science Department on Rate My Professors
Source Type: Rate My Professors department search page
URL or Description: Rate My Professors Computer Science department page for Caldwell University

Content:
The Rate My Professors Computer Science department search page for Caldwell University lists 19 professors. Visible professors include Arnold Toffler, Vladislav Veksler, Isaac Damoah, Michael Koskinen, and Gary Lieberman.

Visible summary ratings:
- Arnold Toffler: quality 3.5, 30 ratings, 60% would take again, 2.7 difficulty.
- Vladislav Veksler: quality 5.0, 4 ratings, 100% would take again, 1.3 difficulty.
- Isaac Damoah: quality 4.6, 19 ratings, 100% would take again, 2.0 difficulty.
- Michael Koskinen: quality 3.6, 4 ratings, 50% would take again, 2.0 difficulty.
- Gary Lieberman: quality 3.3, 4 ratings, 0% would take again, 3.0 difficulty.

Useful facts for RAG:
- The page gives a department-level comparison of Caldwell CS professors.
- Vladislav Veksler has the highest visible quality rating among these listed professors.
- Arnold Toffler has the highest visible number of ratings among these listed professors.
- Gary Lieberman has the highest visible difficulty score among these listed professors.
""",

    "caldwell_cs_program.txt": """Source Name: Caldwell University Computer Science Program
Source Type: Official Caldwell University webpage
URL or Description: https://www.caldwell.edu/programs/computer-science/

Content:
Caldwell University's Bachelor of Science in Computer Science prepares students for a technology career with a strong foundation in computer programming and focused electives.

Important courses listed on the page include:
- CS 195 Computer Programming I
- CS 196 Computer Programming II
- MA 140 Discrete Mathematical Structures
- MA 311 Probability and Statistics I
- CS 225 Introduction to Operating Systems
- CS 230 Front-End Web Development
- CS 231 Responsible Technology in a Digital Society
- CS 238 E-Commerce
- CS 240 Windows Programming
- CS 327 Internet and Enterprise Security
- CS 332 Student Information Technology Experiential Learning
- CS 334 Computer Forensics I
- CS 340 Introduction to Data Science
- CS 355 Full-Stack Web Development
- CS 360 Mobile Development
- CS 415 Computational Models and Simulations
- CS 420 Artificial Intelligence
- CS 487 Field Internship I
- CS 491 Undergraduate Research I

Useful facts for RAG:
- The CS major includes programming, systems, web development, data science, AI, internship, and research opportunities.
- CS 195 and CS 196 are foundational programming courses.
- CS 340 is the data science course.
- CS 420 is the artificial intelligence course.
""",

    "caldwell_cs_department.txt": """Source Name: Caldwell University Computer Science and Information Systems Department
Source Type: Official Caldwell University webpage
URL or Description: https://www.caldwell.edu/academics/academic-departments/dept-computer-science-info-systems/

Content:
The Computer Science and Information Systems Department at Caldwell University equips students with skills, competencies, and mindsets needed to succeed in technology. The department says faculty combine professional experience with academic expertise and bring real-world experience into the classroom.

The department lists several pathways.

Majors:
- Computer Science
- Computer Information Systems
- Business Analytics

Minors:
- Computer Science
- Management Information Systems
- Business Analytics
- Human-Computer Interaction

The department also mentions Caldwell C-STEM Laboratories. C-STEM supports Computational STEM programs, including artificial intelligence and neuroscience research, software development, robotics and engineering projects, clubs, workshops, competitions, and events.

Student clubs and activities mentioned include:
- Google Developers Group on Campus
- Robotics Club
- Computer Science Club
- Women in STEM Club
- Science Club

Useful facts for RAG:
- Caldwell offers CS-related majors and minors.
- The department connects CS with business analytics, MIS, HCI, AI, neuroscience research, robotics, software development, and student clubs.
""",

    "caldwell_cs_faculty.txt": """Source Name: Caldwell University Computer Science and Information Systems Faculty and Staff
Source Type: Official Caldwell University webpage
URL or Description: Caldwell University faculty and staff page for School of Business and Computer Science

Content:
The Caldwell University faculty and staff information gives official background about people in the School of Business and Computer Science.

Salvatore Ferraro is listed as Associate Professor and Chair. His background includes management information systems, organizational leadership, and professional experience across manufacturing, telecommunications, healthcare, shipping, and aerospace.

Steven E. Kreutzer is listed as Associate Professor of Computer Science. His background includes computer science education and a long industry career. His professional experience includes product management, business analysis, software development, and project management. The faculty page says he has taught more than a dozen computer science courses and focuses on preparing students for successful careers.

Bella Veskler is listed as an Adjunct Lecturer. Her background includes computer science, psychology, and cognitive science.

Useful facts for RAG:
- The faculty page provides official faculty background information.
- Steven Kreutzer has software development, business analysis, product management, and project management experience.
- Salvatore Ferraro has MIS and broad industry experience.
- Bella Veskler has computer science and cognitive science background.
""",

    "caldwell_cs_four_year_plan.txt": """Source Name: Caldwell University Computer Science Suggested Four-Year Major Plan
Source Type: Official Caldwell University PDF/course planning document
URL or Description: Caldwell University Computer Science suggested four-year major plan PDF

Content:
The Caldwell University Computer Science suggested four-year major plan lists major requirements for the Bachelor of Science in Computer Science.

Courses shown in the plan include:
- CS 195 Computer Programming I
- CS 196 Computer Programming II
- CS 216 Data Structures and Algorithms
- CS 225 Operating Systems
- CS 301 Computer Organization and Architecture
- CS 302 Design and Analysis of Algorithms
- CS 320 Networking and Communications
- CS 322 Programming Languages and Paradigms
- CS 420 Artificial Intelligence
- CS 450 Software Engineering
- CS 200+ electives at the 200 level or higher
- CS 487 Internship, encouraged

The plan also mentions:
- Total credits required minimum: 120 credits
- Minimum GPA: 2.0
- Minimum grade in major courses: C
- Students may need CS 115 Essential Computer Skills before beginning the Computer Science major sequence if they do not pass the waiver test.

Useful facts for RAG:
- The four-year plan gives official course sequence context.
- CS 216 is Data Structures and Algorithms.
- CS 420 is Artificial Intelligence.
- CS 450 is Software Engineering.
- CS 487 Internship is encouraged.
"""
}

for filename, content in docs.items():
    path = RAW_DIR / filename
    path.write_text(content.strip() + "\n", encoding="utf-8")

print(f"Created/updated {len(docs)} documents in {RAW_DIR}")
for file in sorted(RAW_DIR.glob("*.txt")):
    print(f"{file.name}: {file.stat().st_size} bytes")