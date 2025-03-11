class Rules:
    
    def create_rules(self) -> list:
        return [
    {
        "condition": lambda facts: facts["cloth_type"] == "Верхняя"
                                   and facts["dirty_strong"] == "Сильно"
                                   or facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Белый"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для белой одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Верхняя"
                                   and facts["dirty_strong"] == "Сильно"
                                   or facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Цветная"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для цветной одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Верхняя"
                                   and facts["dirty_strong"] == "Слабо"
                                   or facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Белый"
                                   and facts["user_prefers"] == "Долгая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для белой одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Верхняя"
                                   and facts["dirty_strong"] == "Слабо"
                                   and facts["is_prints"] == "Нет"
                                   and facts["cloth_color"] == "Белый"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - быстрая стирка со средством для белой одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Верхняя"
                                   and facts["dirty_strong"] == "Сильно"
                                   and facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Белый"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для белой одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Верхняя"
                                   and facts["dirty_strong"] == "Сильно"
                                   and facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Цветная"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для цветной одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Нижняя"
                                   and facts["dirty_strong"] == "Сильно"
                                   and facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Белый"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для белой одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Нижняя"
                                   and facts["dirty_strong"] == "Слабо"
                                   and facts["is_prints"] == "Нет"
                                   and facts["cloth_color"] == "Цветная"
                                   and facts["user_prefers"] == "Долгая стирка",
        "action": lambda facts: "Рекомендуемый режим - быстрая стирка со средством для цветной одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Нижняя"
                                   and facts["dirty_strong"] == "Сильно"
                                   and facts["is_prints"] == "Нет"
                                   and facts["cloth_color"] == "Белый"
                                   and facts["user_prefers"] == "Долгая стирка",
        "action": lambda facts: "Рекомендуемый режим - долгая стирка со средством для белой одежды"
    },
    {
        "condition": lambda facts: facts["cloth_type"] == "Нижняя"
                                   and facts["dirty_strong"] == "Слабо"
                                   and facts["is_prints"] == "Есть"
                                   and facts["cloth_color"] == "Цветная"
                                   and facts["user_prefers"] == "Быстрая стирка",
        "action": lambda facts: "Рекомендуемый режим - быстрая стирка со средством для цветной одежды"
    }
]


    def input_facts(self) -> dict:
        return {
            "cloth_type": input("Введите тип одежды (Верхняя / Нижняя) "),
            "dirty_strong": input("Введите степень загрязнения (Сильно / Слабо) "),
            "is_prints": input("Есть ли пятна на одежде? (Есть / Нет) "),
            "cloth_color": input("Введите цвет одежды (Белый / Цветная) "),
            "user_prefers": input("Какую стирку предпочитаете вы? (Быстрая стирка / Долгая стирка) ")
        }