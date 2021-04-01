.PHONY: all install venv test test-all run clean pack doc

VENV := venv
ZIP_NAME:=xsafar23_xmudra04_xparil04_xkrizo05

all:

install: venv

$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || (python3 -m venv $(VENV))
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

test: venv
	./$(VENV)/bin/pytest math_lib_tests.py --verbose || true

test-all: venv
	./$(VENV)/bin/pytest math_lib_tests.py math_interpreter_tests.py --verbose || true

run: venv
	./$(VENV)/bin/python3 gui.py

doc:

clean:
	rm -f -R ./$(VENV)
	rm -f -R ./.pytest_cache
	rm -f -R $(ZIP_NAME)

pack: clean
	mkdir $(ZIP_NAME) && cd $(ZIP_NAME) && mkdir doc repo install
	cd $(ZIP_NAME)/repo && git clone https://github.com/SafarMirek/FITCalcPro.git .
	zip -r $(ZIP_NAME) $(ZIP_NAME)

