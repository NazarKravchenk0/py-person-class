class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    # create Person instances
    persons = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    # link wife/husband attributes
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            setattr(person, "wife", Person.people[person_dict["wife"]])
        if "husband" in person_dict and person_dict["husband"] is not None:
            setattr(person, "husband", Person.people[person_dict["husband"]])
    return persons
