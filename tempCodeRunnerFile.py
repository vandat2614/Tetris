    def play_music(self):
        pygame.mixer.music.play(-1, self.start)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.start = pygame.mixer.music.get_pos() / 1000.0