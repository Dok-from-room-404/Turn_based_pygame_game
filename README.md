# Turn_based_pygame_game
# Hello little friends. Welcome to start game development
# Лаунчер на время вырезан (чтобы лишний раз не раздражал)
# Задачи:
#   1) При добавленни большого количества врагов, враги при перемещении ломают игру из-за чего возбуждается исключение KeyError
#   2) Необходимо добавить отображение save point (текстура не отображается на карте ) (TheRealPumpkin)
#   3) Для save point необходимо добавить сохранение уровня (в сохранение отображается индекс нового уровня) и переход на новый уровень. (TheRealPumpkin)
#   4) Необходимо создать меню для выбора сохранения (Room 404)

№ 1 (потробности):
    File "...\Проект игра\Turn_based_pygame_game\main.py", line 148, in <module>
      main()
    File "...\Проект игра\Turn_based_pygame_game\main.py", line 138, in main
      program_main.launcher()
    File "...\Проект игра\Turn_based_pygame_game\main.py", line 26, in launcher
      self.game(size, fps, block_size)
    File "...\Проект игра\Turn_based_pygame_game\main.py", line 126, in game
      game.run(screen)
    File "...\Проект игра\Turn_based_pygame_game\Game\__init__.py", line 93, in run
      self.board.update()
    File "...\Проект игра\Turn_based_pygame_game\Game\Board.py", line 56, in update
      enemy.action()
    File "...\Проект игра\Turn_based_pygame_game\Game\Sprites.py", line 75, in action
      self.make_move()
    File "...\Проект игра\Turn_based_pygame_game\Game\Sprites.py", line 82, in make_move
      cur_move = visited[cur_move]
KeyError: (18, 3)