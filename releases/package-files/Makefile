.PHONY: all install clean

DESTDIR = $(HOME)
SHELL = /bin/bash
INSFLAGS = -m 0755

vpath %.py ../../src
vpath help.pdf ../../src
vpath dokumentace.pdf ../..

all: dist/FITCalcPro

dist/FITCalcPro: gui.py
	pyi-makespec ../../src/gui.py --onefile -n "FITCalcPro"
	pyinstaller FITCalcPro.spec
	
dist/dokumentace.pdf: dokumentace.pdf
	cp ../../dokumentace.pdf $@
	
dist/help.pdf: help.pdf
	cp ../../src/help.pdf $@
	
install: dist/FITCalcPro dist/help.pdf dist/dokumentace.pdf
	mkdir -p $(DESTDIR)/opt/fitcalcpro
	cd dist; find * -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/fitcalcpro/{}" \;

clean:
	rm -f -R ./build
	rm -f -R ./dist
	rm -f FITCalcPro.spec

