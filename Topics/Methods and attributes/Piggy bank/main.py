class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents

        # Handle cents overflow
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents %= 100