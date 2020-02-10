'''################################
## This is the method to be used ##
###################################'''


def getVigentFacts(facts, schema):
    data = {}
    cardinality = get_cardinality(schema)
    for index, fact in enumerate(facts):
        addFactToData(fact, data, cardinality, index)
    vigentFacts = []
    vigentFacts = convertDataToFactStructure(data)
    return vigentFacts

 '''################################
## All methods above are auxiliary ##
###################################'''


def addFactToData(fact, data, cardinality, index):
    entity = fact[0]
    attributeKey = fact[1]
    attributeValue = (fact[1], fact[2], fact[3], index)
    isAddOperation = fact[-1]
    if entity in data:
        consume_fact(attributeKey, data, entity, isAddOperation, cardinality,
                     attributeValue)
    else:
        create_entity(data, entity)
        consume_fact(attributeKey, data, entity, isAddOperation, cardinality,
                     attributeValue)


def consume_fact(attributeKey, data, entity, isAddOperation, cardinality,
                 atributeValue):
    if attributeKey in data[entity]:
        if isAddOperation:
            add_value_to_attribute(cardinality, attributeKey, data, entity,
                                   atributeValue)
        else:
            remove_value_from_attribute(atributeValue, data, entity,
                                        attributeKey)
    elif isAddOperation:
        create_attribute(data, entity, attributeKey)
        add_value_to_attribute(cardinality, attributeKey, data, entity,
                               atributeValue)


def create_attribute(data, entity, attributeKey):
    data[entity][attributeKey] = []


def create_entity(data, entity):
    data[entity] = {}


def add_value_to_attribute(cardinality, attributeKey, data, entity,
                           atributeValue):
    if is_cardinalityOne(cardinality, attributeKey):
        data[entity][attributeKey].clear()
    data[entity][attributeKey].append(atributeValue)


def remove_value_from_attribute(attributeValue, data, entity, attributeKey):
    oldList = data[entity][attributeKey]
    data[entity][attributeKey] = [attribute for attribute in oldList if
                                  attribute[1] != attributeValue[1]]


def is_cardinalityOne(cardinality, attributeKey):
    return cardinality[attributeKey][0] == "one"


def get_cardinality(schema):
    cardinality = {}
    for a, _, c in schema:
        cardinality.setdefault(a, []).append(c)
    return cardinality


def convertDataToFactStructure(data):
    validFacts = []
    for entity, attributes in data.items():
        for _, values in attributes.items():
            for fact in values:
                validFacts.append((entity, fact[0], fact[1], fact[2], fact[3]))
    validFacts.sort(key=lambda x: x[-1])
    validFacts = [f[0:-1] for f in validFacts]
    return validFacts
