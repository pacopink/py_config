#!/usr/bin/env python3

from config.OrderedDictJsonYaml import GenericItem

class Person(GenericItem):
    def __init__(self):
        """
        self.name = None
        self.id = None
        self.age = None        
        """
        pass

class Company(GenericItem):
    def __init__(self):
        self.boss: Person = None
        self.members:list(Person) = None

    def attr_to_convert_to_list(self):
        return (('members', Person),)

    def attr_to_convert(self):
        return (('boss', Person),)

if __name__=='__main__':
    company = Company.make_from_file("test.yml")
    print(company.yamlize())
    with open("test.json", "w", encoding='utf8') as f:
        f.write(company.jsonify())
    company1 = Company.make_from_file("test.json")
    print(company1.yamlize())
    print(company1.jsonify(indent=2))
