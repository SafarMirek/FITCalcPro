.PHONY: all install clean

DESTDIR = $(HOME)
SHELL = /bin/bash
INSFLAGS = -m 0755

vpath %.py ../../src
vpath help.pdf ../../src
vpath user_documentation.pdf ../..

all: dist/FITCalcPro

dist/FITCalcPro: gui.py
	pyi-makespec ../../src/gui.py --onefile -n "FITCalcPro"
	pyinstaller FITCalcPro.spec
	
dist/user_documentation.pdf: user_documentation.pdf
	cp ../../user_documentation.pdf $@
	
dist/help.pdf: help.pdf
	cp ../../src/help.pdf $@
	
install: dist/FITCalcPro dist/help.pdf dist/user_documentation.pdf
	mkdir -p $(DESTDIR)/opt/fitcalcpro
	cd dist; find * -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/fitcalcpro/{}" \;

clean:
	rm -f -R ./build
	rm -f -R ./dist
	rm -f FITCalcPro.spec

