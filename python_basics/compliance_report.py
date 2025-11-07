project_data = [
    {
        "project_id": "PJT-900",
        "budget_history": (10500.0, 12000.0, 18000.0),
        "team_members": {"A101", "B202", "C303", "D404"},
        "required_skills": ["Python", "Cloud"],
        "is_on_time": True,
    },
    {
        "project_id": "PJT-901",
        "budget_history": (5000.0, 4000.0, 3000.0),
        "team_members": {"E505", "F606"},
        "required_skills": ["C++", "SQL"],
        "is_on_time": False,
    },
    {
        "project_id": "PJT-902",
        "budget_history": (20000.0, 15000.0, 16000.0),
        "team_members": {"G707", "H808", "I909"},
        "required_skills": ["Java", "Design"],
        "is_on_time": True,
    },
]

master_skills = {"Python", "Java", "SQL", "Cloud", "Design"}


def generate_report(projects: list):

    temp = {}

    for project in projects:
        id = project["project_id"]
        budget_pass = all(
            [
                sum(project["budget_history"]) < 50000.0,
                any(budget > 15000.0 for budget in project["budget_history"]),
            ]
        )
        skills_pass = (
            True if set(project["required_skills"]).issubset(master_skills) else False
        )
        perf_pass = (
            True
            if len(project["team_members"]) > 3 or project["is_on_time"] is True
            else False
        )
        d = {
            id: {
                "Status": "",
                "Budget_Pass": budget_pass,
                "Skills_Pass": skills_pass,
                "Performance_Pass": perf_pass,
            }
        }
        if sum([skills_pass, budget_pass, perf_pass]) == 3:
            d[id]["Status"] = "Fully Compliant"
        elif sum([skills_pass, budget_pass, perf_pass]) == 0:
            d[id]["Status"] = "Non-Compliant"
        else:
            d[id]["Status"] = "Partially Compliant"

        temp.update(d)
    return temp


print(generate_report(project_data))
