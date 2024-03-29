from .base_command import BaseCommand


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class Help(BaseCommand):
    def __init__(self):
        description = "Displays this help message."
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        from message_handler import COMMAND_HANDLERS

        msg = message.author.mention + "\n"
        msg += "\n:man_mage:  _NOTE_\n - `variable*` mean variable is mendatory (asterisk)\n - `variable:default` is for optionnal variables with their default state.\n\n"

        # Displays all descriptions, sorted alphabetically by command name
        for cmd in sorted(COMMAND_HANDLERS.items()):
            msg += "\n" + cmd[1].description

        await message.channel.send(msg)
