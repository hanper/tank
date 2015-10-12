import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name = "SNAKE MONSTER",
    options = {"build_exe": {"packages": ["pygame"], "include_files":["snake_head_30.png", "snake_head_20.png", "apple.png"]}},
    description = "SNAKE game test",
    executables = executables
    )
