def calculate_score(user, scheme):

    score = 0

    if scheme["occupation"] == "Any":
        score += 30

    elif (
        scheme["occupation"].lower()
        == user["occupation"].lower()
    ):
        score += 50

    if user["income"] <= scheme["income_max"]:
        score += 50

    return min(score, 100)