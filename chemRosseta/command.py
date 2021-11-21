# author: Roy Kid
# contact: lijichen365@126.com
# date: 2021-11-21
# version: 0.0.1

class Command:
    
    commands = []
    
    def __init__(self) -> None:
        Command.commands.append(self)