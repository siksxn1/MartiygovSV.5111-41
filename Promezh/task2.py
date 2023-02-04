#Создаём класс основания
class blades:
    #Бренд основания.
    name: str
    #Модель основания.
    model: str
    #Скорость основания.
    speed: float
    #Вибрация основания.
    vibration: float
    
    #Количесвто слоев.
    layers: float

    def __init__(self, name: str = "Без названия", model: str = "Не установлено", speed: float = 0, vibration: float = 0, layers: float = 0):
        self.name = name
        self.model = model
        self.speed = speed
        self.vibration = vibration
        self.layers = layers


class rubbers:
    # Бренд накладки.
    name: str
    # Модель накладки.
    model: str
    # Скорость накладки.
    speed: float
    # Вращение накладки.
    spin: float
    # Жёсткость накладки
    rigidity: float


    def __init__(self, name: str = "Без названия", model: str = "Не установлено", speed: float = 0, spin: float = 0, rigidity: float = 0):
        self.name = name
        self.model = model
        self.speed = speed
        self.spin = spin
        self.rigidity = rigidity

Rubbers1 = rubbers("Butterfly", "Tenergy05", 13, 36, 11.5)
Rubbers2 = rubbers("Butterfly", "Tenergy64", 13.5, 36, 10.5)
Blades1 = blades("Butterfly", "Harimoto", 12, 8, 7)
Blades2 = blades("Butterfly", "Ovcharov", 10, 12, 5)


#скорость ракетки
l = [Rubbers1,Blades2]
print(sum([x.speed for x in l]))








