class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    # create Person instances
    persons = [Person(p["name"], p["age"]) for p in people]

    # link wife/husband attributes
    for p in people:
        person = Person.people[p["name"]]
        if "wife" in p and p["wife"] is not None:
            setattr(person, "wife", Person.people[p["wife"]])
        if "husband" in p and p["husband"] is not None:
            setattr(person, "husband", Person.people[p["husband"]])
    return persons
