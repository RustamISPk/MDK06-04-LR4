from Rules import Rules

def final_verdict(rules: list, facts: dict) -> str:
    for rule in rules:
        if rule["condition"](facts):
            return rule["action"](facts)
    return "Ошибка запроса"

rulesAndFacts = Rules()
systemRules = rulesAndFacts.create_rules()

systemFacts = rulesAndFacts.input_facts()
result = final_verdict(systemRules, systemFacts)

print(result)
