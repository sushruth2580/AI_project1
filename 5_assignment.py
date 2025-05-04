import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# ----------- Job Description & Resume Inputs -----------
job_description = """
5+ years hands-on experience in implementing solutions using Java/J2EE, Spring framework (Batch framework), Angular, API Development (REST), 
Rules Engine (DROOLS). 2+ years hands-on experience in working with Cloud technologies (Microsoft Azure preferred) - features like Azure ASB, 
Azure functions, Azure Gateway, File Storage etc. 3 years of Python development experience a plus. 
Proven experience working with Code Quality and Code Coverage tools and frameworks (e.g. Sonar). 
Strong programming, debugging and secure software development skills. 
Strong knowledge of CI/CD and DevOps (specifically Jenkins, UDeploy, GIT). 
Familiarity with Test Driven Development. 
Strong understanding of Java development environment and standard methodologies, such as Maven, Sonar, Bitbucket security and other Open-Source tools.
"""

sample_resume = """
JAVA DEVELOPER RESUME

Name: John Doe
Email: john.doe@example.com
Phone: +1-123-456-7890
LinkedIn: linkedin.com/in/johndoe
GitHub: github.com/johndoe
Location: San Francisco, CA (Willing to relocate)

PROFESSIONAL SUMMARY
Skilled Java Developer with 5 years of hands-on experience in designing, developing, and maintaining enterprise-level applications using Java, 
Spring Boot, and React.js. Proficient in integrating front-end interfaces with robust back-end APIs, optimizing database performance, and applying 
modern CI/CD pipelines. Strong experience with Agile/Scrum development and a passion for writing clean, maintainable code with comprehensive test coverage.

TECHNICAL SKILLS
• Languages: Java, JavaScript, SQL, HTML, CSS
• Frameworks/Libraries: Spring Boot, Hibernate, React.js, Redux
• Databases: MySQL, PostgreSQL, MongoDB
• Tools: Git, Maven, Jenkins, Docker, JUnit, Postman
• CI/CD: Jenkins, GitLab CI, Docker, Kubernetes (basic)
• Testing: JUnit, Mockito, Selenium, REST-assured
• Cloud: AWS (EC2, S3), basic GCP knowledge
• Version Control: Git, GitHub, GitLab
• Methodologies: Agile (Scrum), TDD, RESTful API design

PROFESSIONAL EXPERIENCE

Software Engineer | ABC Tech Solutions, San Francisco, CA
May 2021 – Present
• Developed and maintained microservices using Java, Spring Boot, and Hibernate.
• Created responsive web interfaces using React.js and Redux.
• Integrated RESTful APIs with front-end components for dynamic functionality.
• Optimized SQL queries and improved database performance in PostgreSQL.
• Implemented CI/CD pipelines with Jenkins and Docker, reducing release cycles by 30%.
• Automated test cases with JUnit, Mockito, and Selenium to improve code reliability.
• Participated in Agile ceremonies and conducted peer code reviews.

Java Developer | XYZ Systems Inc., San Jose, CA
April 2019 – April 2021
• Built backend services in Java and connected to MongoDB and MySQL databases.
• Developed single-page applications using React.js and integrated with REST APIs.
• Collaborated with QA to define testing strategies using JUnit and REST-assured.
• Used Git and GitLab for version control and continuous integration.
• Deployed applications to AWS EC2 instances and managed environments using Docker.

EDUCATION
Bachelor of Science in Computer Science
University of California, Santa Cruz | 2015 – 2019

CERTIFICATIONS
• Oracle Certified Java Programmer (OCJP)
• AWS Certified Developer – Associate (In Progress)
"""

# ----------- Prompt for Evaluation -----------
messages = [
    {
        "role": "system",
        "content": (
            "Evaluate the resume against the job description. "
            "Match relevant tools, technologies, and required skills. "
            "Generate a one-page report outlining matching points, missing elements, and overall fit. "
            "Conclude with a clear verdict: Is the candidate suitable for the role or not?"
        )
    },
    {
        "role": "user",
        "content": (
            f"Resume:\n{sample_resume}\n\n"
            f"Job Description:\n{job_description}"
        )
    }
]

# ----------- Call GPT Model -----------
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0
)

# ----------- Output Result -----------
evaluation_report = response.choices[0].message.content.strip()
print("\n Resume Evaluation Report:\n")
print(evaluation_report)
