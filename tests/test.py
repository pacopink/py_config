#!/usr/bin/env python3

from yaml_json_config_paco.OrderedDictJsonYaml import GenericItem

class Company0(GenericItem):
    """shallow load demo"""
    pass

class Person(GenericItem):
    def __init__(self):
        self.name = None
        self.id = None
        self.age = None        

class Company(GenericItem):
    def __init__(self):
        self.boss: Person = None
        self.members:list(Person) = None

    def attr_to_convert_to_list(self):
        return (('members', Person),)

    def attr_to_convert(self):
        return (('boss', Person),)

if __name__=='__main__':
    company0 = Company0.from_file("sample.yml") 
    print(company0.address)
    print(company0.telephone)
    print(company0.boss)
    print(company0.members)
    #company = Company.from_file("sample.yml")
    #print(company.yamlize())
    #with open("sample.json", "w", encoding='utf8') as f:
    #    f.write(company.jsonify())
    #company1 = Company.from_file("sample.json")
    #print(company1.yamlize())
    #print(company1.jsonify(indent=2))
