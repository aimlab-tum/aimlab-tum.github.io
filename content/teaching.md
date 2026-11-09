+++
# /teaching/. The programme band, the courses and the theses box are data
# below; the text after the front matter is the introduction (its first
# paragraph also opens the Teaching section of the homepage) and the two
# notes shown under the courses.
#
# Adding a semester is one `[[semesters]]` block at the top of the list; the
# first one is shown open, the rest fold away under "Earlier semesters". A
# course is one `[[semesters.courses]]` block: `type` (Practical, Lecture or
# Seminar), `title`, `code`, optionally `url` and a `note`.
title = "Teaching"
layout = "teaching_page"

[programme]
  eyebrow = "Elite Master's programme"
  title = "AI in Biomedicine"
  text = """
Our chair takes part in this Elite Master's programme, with Prof. Daniel Rückert as programme speaker. A research-oriented two-year degree at TUM in cooperation with Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU), it bridges computer science, engineering and medicine to train AI experts who pair technical depth with biomedical domain knowledge, and prepares them for academic research and industry.

An optional Research Excellence Certificate is available.
"""
  url = "https://www.cit.tum.de/en/cit/studies/degree-programs/ai-in-biomedicine/"
  contact = "app-msaibm.asa@xcit.tum.de"
  [[programme.facts]]
    label = "Degree"
    value = "Master's, two years, research-oriented"
  [[programme.facts]]
    label = "Partners"
    value = "TUM and FAU Erlangen-Nürnberg"
  [[programme.facts]]
    label = "Programme speaker"
    value = "Prof. Daniel Rückert"
  [[programme.facts]]
    label = "Applications"
    value = "February 1 – May 31, every year"

[theses]
  eyebrow = "Work with us"
  title = "Theses, internships and student positions"
  text = "In addition to lectures, seminars, and internships, we offer a range of bachelor's, master's and IDP projects. All current openings are listed on the CIT thesis portal."
  url = "https://thesis.aet.cit.tum.de/?groups=c9a54897-40cb-4cdb-87ce-171f33b0a7e2"
  action = "Browse our open projects"

[[semesters]]
  name = "Winter semester 2026/27"
  [[semesters.courses]]
    type = "Practical"
    title = "Applied Deep Learning in Medicine"
    url = "https://kiinformatik.mri.tum.de/de/practicalalex"
    code = "IN2106, IN4314"
  [[semesters.courses]]
    type = "Lecture"
    title = "Künstliche Intelligenz in der Medizin I"
    code = "IN2403"
  [[semesters.courses]]
    type = "Lecture"
    title = "Foundations of AI in Biomedicine"
    code = "CIT423005"
    note = "exclusively for AI in Biomedicine students"
  [[semesters.courses]]
    type = "Lecture"
    title = "Multimodal AI in Medicine"
    code = "CIT423009"
  [[semesters.courses]]
    type = "Lecture"
    title = "Trustworthy AI for Medicine"
    code = "CIT423007"
  [[semesters.courses]]
    type = "Seminar"
    title = "Research Skills and Methods"
    code = "CIT422000"
    note = "exclusively for AI in Biomedicine students"
  [[semesters.courses]]
    type = "Seminar"
    title = "Master's Seminar: Large Language Models in Medicine"
    code = "IN2107"
  [[semesters.courses]]
    type = "Seminar"
    title = "Master's Seminar: AI Research in the Large Language Models Era"
    code = "IN2107"

[[semesters]]
  name = "Summer semester 2026"
  [[semesters.courses]]
    type = "Practical"
    title = "Applied Deep Learning in Medicine"
    url = "https://kiinformatik.mri.tum.de/de/practicalalex"
    code = "IN2106, IN4314"
  [[semesters.courses]]
    type = "Lecture"
    title = "Artificial Intelligence in Medicine II"
    code = "IN2408"
  [[semesters.courses]]
    type = "Seminar"
    title = "Implicit Neural Representation and Neural Fields"
    url = "https://kiinformatik.mri.tum.de/de/seminarharvey"
    code = "IN2107"
  [[semesters.courses]]
    type = "Seminar"
    title = "Deep Learning for Inverse Problems in Medical Imaging"
    url = "https://kiinformatik.mri.tum.de/de/seminarsevgi"
    code = "IN2107"

[[semesters]]
  name = "Winter semester 2025/26"
  [[semesters.courses]]
    type = "Practical"
    title = "Applied Deep Learning in Medicine"
    url = "https://kiinformatik.mri.tum.de/de/practicalalex"
    code = "IN2106, IN4314"
  [[semesters.courses]]
    type = "Lecture"
    title = "Künstliche Intelligenz in der Medizin I"
    code = "IN2403"
  [[semesters.courses]]
    type = "Lecture"
    title = "Multi-modal AI in Medicine"
    code = "CIT423009"
  [[semesters.courses]]
    type = "Seminar"
    title = "Trustworthy AI for Medicine"
    code = "IN2107, IN45048"
  [[semesters.courses]]
    type = "Seminar"
    title = "Multi-modal AI for Medicine"
    url = "https://kiinformatik.mri.tum.de/de/seminarharvey-multi-modal-ai-medicine"
    code = "IN2107, IN45072"
+++

Teaching and education are an integral part of our institute's mission. All of our courses—which are heavily influenced by our research—are taught in English. We offer lectures for students from various disciplines, but our core lectures are aimed at computer science students:

Practicals and seminars take the individual subject areas further, with students applying what they learn in direct contact with our lecturers.

For medical students we offer the elective **Computer Science for Medical Students**: AI methods, above all neural networks, and their use in medicine. Students learn the theory, write their first Python, and train a network of their own.
