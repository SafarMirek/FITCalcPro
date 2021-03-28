
class ButtonAction:
    def __init__(self, name, format_text, operation, instant):
        self.name = name
        self.format_text = format_text
        self.operation = operation
        self.instant = instant

    def get_formatted(self, text):
        return self.format_text.replace("{value}", text)


class RootButtonAction(ButtonAction):
    def __init__(self, name, format_text, operation, tosuperscript_fce):
        super().__init__(name, format_text, operation, False)
        self.tosuperscript_fce = tosuperscript_fce

    def get_formatted(self, text):
        return self.tosuperscript_fce(text) + u"\u221a\u25a1"


