##
# @file ButtonActions.py
# @brief definuje akci funkčních tlačítek
# @author Miroslav Šafář <xsafar23.stud.fit.vutbr.cz>
#
# * Project: fit-ivs-2
# * Date created: 2021-03-29
# * Last modified: 2021-04-23
#

##
# @class ButtonAction
# @brief Obecná akce funkčního tlačítka
#
class ButtonAction:
    ##
    # @brief Konstruktor
    # @param name jméno prováděné funkce
    # @param format_text formát textu pro zpracování
    # @param operation operace která se provádí
    # @param instant určuje, zda se funkce provede okamžitě nebo ne
    # @param implicit_value pokud není zadán vstupní parametr
    #
    def __init__(self, name, format_text, operation, instant, implicit_value=None):
        ## jméno prováděné funkce
        self.name = name
        ## formát textu pro zpracování
        self.format_text = format_text
        ## operace která se provádí
        self.operation = operation
        ## určuje, zda se funkce provede okamžitě nebo ne
        self.instant = instant
        ## pokud není zadán vstupní parametr
        self.implicit_value = implicit_value

    ##
    # @brief Převede objekt na řetězec
    # @return formátovací řetězec
    #
    def __str__(self):
        return self.format_text

    ##
    # @brief Získá naformátovaný řetězec funkce
    # @param value vstupní parametr funkce
    # @return zformátovaná funkce
    #
    def get_formatted(self, value):
        return self.format_text.replace("{value}", value)

    ##
    # @brief Zjistí, jestli má funkce implicitní hodnotu
    # @return true, pokud má, false, pokud nemá
    #
    def has_implicit_value(self):
        return self.implicit_value is not None

##
# @class CustomButtonAction
# @brief Akce funkčního tlačítka s podporou vlastního formátování
#
class CustomButtonAction(ButtonAction):
    ##
    # @brief Konstruktor
    # @param name jméno prováděné funkce
    # @param format_text formát textu pro zpracování
    # @param operation operace která se provádí
    # @param to_superscript_fce formátovací funkce
    #
    def __init__(self, name, format_text, operation, to_superscript_fce):
        super().__init__(name, format_text, operation, False)
        ## formátovací funkce
        self.to_superscript_fce = to_superscript_fce

##
# @class PiButtonAction
# @brief Akce tlačítka pi
#
class PiButtonAction(ButtonAction):

    ##
    # @brief Přeformátuje posledního člena
    # @param value vstupní parametr funkce
    #
    def get_formatted(self, value):
        if value == "1":
            ## vstupní parametr funkce
            value = ""
        return super().get_formatted(value)
