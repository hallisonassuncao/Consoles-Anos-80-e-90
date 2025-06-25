class Retro_Gamer:
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
neo_geo = Retro_Gamer()
neo_geo.POWER_ON()
neo_geo.LOAD_NO_CARTUCHO("STREET OF RAGE 2")
neo_geo.PRESS_START()
neo_geo.GAME_OVER()