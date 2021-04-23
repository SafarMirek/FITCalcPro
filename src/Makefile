.PHONY: all install venv test test-all run clean pack doc installer

VERSION := 1.0

DOC_DIR := dokumentace
VENV := venv
ZIP_NAME:=xsafar23_xmudra04_xparil04_xkrizo05

all: venv

install: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m pip install virtualenv
	test -d $(VENV) || (python3 -m venv $(VENV))
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

test: venv
	./$(VENV)/bin/pytest math_lib_tests.py --verbose || true

test-all: venv
	./$(VENV)/bin/pytest --verbose || true

run: venv
	./$(VENV)/bin/python3 gui.py

doc:
	doxygen Doxyfile

profile: venv

installer:
	python3 -m pip install -r requirements.txt
	python3 -m pip install pyinstaller
	cd ../releases && ./release.sh $(VERSION)

clean:
	rm -f -R ./$(VENV)
	rm -f -R ./.pytest_cache
	rm -f -R ./__pycache__
	rm -f -R $(ZIP_NAME)
	rm -f -R $(ZIP_NAME).zip
	rm -f -R $(DOC_DIR)
	rm -f -R ../releases/fitcalcpro-$(VERSION)
	rm -f ../releases/fitcalcpro-$(VERSION).tar.gx
	rm -f ../releases/fitcalcpro_$(VERSION)_amd64.buildinfo
	rm -f ../releases/fitcalcpro_$(VERSION)_amd64.changes
	rm -f ../releases/fitcalcpro_$(VERSION)_amd64.deb

pack: clean doc installer
	mkdir $(ZIP_NAME) && cd $(ZIP_NAME) && mkdir doc repo install
	cd $(ZIP_NAME)/repo && git clone https://github.com/SafarMirek/FITCalcPro.git .
	cp ../releases/fitcalcpro_$(VERSION)_amd64.deb $(ZIP_NAME)/install/fitcalcpro_$(VERSION)_amd64.deb
	cp -a $(DOC_DIR)/. $(ZIP_NAME)/doc/
	zip -r $(ZIP_NAME) $(ZIP_NAME)

