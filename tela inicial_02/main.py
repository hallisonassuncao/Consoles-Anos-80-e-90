class Hallison_Gamer:
    def __init__(self):
        self.running = False

    def POWER_ON(self):
        print("💾 Ligando console... Tela inicial: PRESS START")
        self.running = True

    def LOAD_NO_CARTUCHO(self, game):
        if self.running:
            print(f"🎮 {game.upper()} carregado com sucesso! Pronto para jogar.")
        else:
            print("⚠️ Ligue o console antes de carregar o cartucho.")

    def PRESS_START(self):
        if self.running:
            print("🔘 Jogo iniciado! Boa sorte!")
        else:
            print(" O console está desligado.")

    def GAME_OVER(self):
        print("💀 Game Over. Insira outro CARTUCHO ou pressione RESET.")
        self.running = False


# Exemplo de uso:
Mega_Drive = Hallison_Gamer()
Mega_Drive.POWER_ON()
Mega_Drive.LOAD_NO_CARTUCHO("STREET OF RAGE 2")
Mega_Drive.PRESS_START()
Mega_Drive.GAME_OVER()