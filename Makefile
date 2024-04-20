PACKAGE_VERSION = $(shell grep -oP 'version": \((.*?)\)' $(CURDIR)/node_note_property_addon/__init__.py | cut -d'(' -f2 | cut -d')' -f1 | sed 's/, /./g')

install_dev:
	@echo "------------------- INSTALL DEV ENV ------------------- "
	rm -rf /tmp/blender/node_note_property_addon
	mkdir /tmp/blender/node_note_property_addon/scripts/addons -p
	ln $(CURDIR)/node_note_property_addon /tmp/blender/node_note_property_addon/scripts/addons/node_note_property_addon -s
	@echo "------------------------------------------------------- "

run:
	@echo "--------------------- RUN BLENDER --------------------- "
	@export BLENDER_USER_SCRIPTS=/tmp/blender/node_note_property_addon/scripts; \
	blender --addons node_note_property_addon

deploy:release
	@echo "------------------- DEPLOY PACKAGE -------------------- "
	@echo Deploying ${PACKAGE_VERSION} version
	@git push --tags
	@gh release create ${PACKAGE_VERSION} ./dist/node_note_property_addon-${PACKAGE_VERSION}.zip --generate-notes --latest 
	@echo "------------------------------------------------------- "

release:build clean
	@echo "------------------- RELEASE PACKAGE ------------------- "
	@echo Releasing ${PACKAGE_VERSION} version
	@git tag ${PACKAGE_VERSION} || echo "Tag already exists."
	@echo "------------------------------------------------------- "

build: clean
	@echo "-------------------- BUILD PACKAGE -------------------- "
	mkdir -p dist
	zip -r dist/node_note_property_addon-${PACKAGE_VERSION}.zip node_note_property_addon
	@echo "------------------------------------------------------- "

clean:
	@echo "-------------------- CLEAN PACKAGE -------------------- "
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	@echo "------------------------------------------------------- "

test:
	python -m unittest discover

coverage:
	coverage run -m unittest discover
	coverage report -m
