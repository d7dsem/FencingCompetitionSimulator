class ScoringValues:
    def __init__(self, clear_hit_value, double_hit_value, afterblow_coast, win_score):
        """
        Ініціалізація класу з заданими значеннями очок для різних типів ударів.

        :param clear_hit_value: Очків для перемоги.
        :param clear_hit_value: Очки за чисте ураження.
        :param double_hit_value: Очки за обопільне ураження.
        :param afterblow_value: Очки за афтерблоу.
        """
        self.clear_hit_value = clear_hit_value
        self.double_hit_value = double_hit_value
        self.afterblow_value = afterblow_coast
        self.win_score = win_score

    def __str__(self):
        return f"Scoring RuleSet(Win Score: {self.win_score} Clear Hit: {self.clear_hit_value}, Double Hit: {self.double_hit_value}, Afterblow: {self.afterblow_value})"
