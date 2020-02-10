import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from TreatFacts import getVigentFacts


def test_add_attribute_and_remove_twice_with_cardinality_many():
    facts = [
        ('joão', 'idade', 18, True),
        ('joão', 'idade', 18, True),
        ('joão', 'idade', 18, False),
     ]
    schema = [('idade', 'cardinality', 'many')]
    vigentFacts = TreatFacts.getVigentFacts(facts, schema)
    if(len(vigentFacts) > 0):
        raise Exception("Fato de retração inserido e não existente não pode \
             ser adicionado")
    assert True


def test_example_from_statment():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]

    expectedFacs = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True)
    ]

    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')
    ]

    vigentFacts = getVigentFacts(facts, schema)
    for expectedFac, fac in zip(expectedFacs, vigentFacts):
        if(expectedFac != fac):
            assert False
    assert True


def test_extended_example_from_statment():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
        ('joão', 'idade', 18, True),
        ('joão', 'idade', 18, False),
        ('joão', 'idade', 18, False),
        ('joão', 'idade', 19, True),
    ]

    expectedFacs = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '91234-5555', True),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
        ('joão', 'idade', 19, True),
    ]

    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many'),
        ('idade', 'cardinality', 'one')
    ]

    vigentFacts = getVigentFacts(facts, schema)
    for expectedFac, fac in zip(expectedFacs, vigentFacts):
        if(expectedFac != fac):
            assert False
    assert True


def test_try_remove_inexisting_attribute():
    facts = [('joão', 'idade', 18, False)]
    schema = [('idade', 'cardinality', 'one')]
    vigentFacts = getVigentFacts(facts, schema)
    if(len(vigentFacts) > 0):
        assert False
    assert True


def add_attribute_and_remove_twice():
    facts = [
        ('joão', 'idade', 18, True),
        ('joão', 'idade', 18, False),
        ('joão', 'idade', 18, False),
     ]
    schema = [('idade', 'cardinality', 'one')]
    vigentFacts = getVigentFacts(facts, schema)
    if(len(vigentFacts) > 0):
        assert False
    assert True


def test_add_attribute_and_remove_twice_with_cardinality_many():
    facts = [
        ('joão', 'idade', 18, True),
        ('joão', 'idade', 18, True),
        ('joão', 'idade', 18, False),
     ]
    schema = [('idade', 'cardinality', 'many')]
    vigentFacts = getVigentFacts(facts, schema)
    if(len(vigentFacts) > 0):
        assert False
    assert True
