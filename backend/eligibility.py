import json


def load_schemes():

    with open("../data/schemes.json", "r", encoding="utf-8") as file:
        return json.load(file)


def check_eligibility(user):

    schemes = load_schemes()

    eligible_schemes = []

    for scheme in schemes:

        occupation_match = (
            scheme["occupation"] == "Any"
            or scheme["occupation"].lower()
            == user["occupation"].lower()
        )

        income_match = (
            user["income"]
            <= scheme["income_max"]
        )

        if occupation_match and income_match:
            eligible_schemes.append(scheme)

    return eligible_schemes