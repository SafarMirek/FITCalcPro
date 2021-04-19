class ButtonAction:
    def __init__(self, name, format_text, operation, instant, implicit_value=None):
        self.name = name
        self.format_text = format_text
        self.operation = operation
        self.instant = instant
        self.implicit_value = implicit_value

    def __str__(self):
        return self.format_text

    def get_formatted(self, value):
        return self.format_text.replace("{value}", value)

    def has_implicit_value(self):
        return self.implicit_value is not None


class CustomButtonAction(ButtonAction):
    def __init__(self, name, format_text, operation, to_superscript_fce):
        super().__init__(name, format_text, operation, False)
        self.to_superscript_fce = to_superscript_fce


class PiButtonAction(ButtonAction):

    def get_formatted(self, value):
        if (value == "1"):
            value = ""
        return super().get_formatted(value)
