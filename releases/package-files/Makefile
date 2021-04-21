.PHONY: all install clean

DESTDIR = $(HOME)
SHELL = /bin/bash
INSFLAGS = -m 0755

vpath %.py ../../src

all: dist/FITCalcPro

dist/FITCalcPro: gui.py
	pyi-makespec ../../src/gui.py --onefile -n "FITCalcPro"
	pyinstaller FITCalcPro.spec
	
install: dist/FITCalcPro
	mkdir -p $(DESTDIR)/opt
	cd dist; find FITCalcPro -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/{}" \;

clean:
	rm -f -R ./build
	rm -f -R ./dist
	rm -f FITCalcPro.spec

