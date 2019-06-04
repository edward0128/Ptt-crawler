PACKAGE_NAME="gpu-management"
VERSION=01-RC3-beta1
tag=v1.0.4

clean::
	rm -rf ./dest/*
	rm -rf ./${VERSION}
	rm -rf ./agena
	rm -rf ./gpu-management/opt/gemini/GPU_management_node

all ::
	@echo "[INFO] Create debian package file (control)."
	rm -rf ./${PACKAGE_NAME}/DEBIAN/control ;\
	cp ./${PACKAGE_NAME}/DEBIAN/control.sample ./${PACKAGE_NAME}/DEBIAN/control ;\
	SIZE=`du -sx --exclude DEBIAN "${PACKAGE_NAME}/DEBIAN/" | awk '{print $$1}'` ;\
	sed -i "s/Installed-Size: 0/Installed-Size: $${SIZE}/g" "./${PACKAGE_NAME}/DEBIAN/control" ;\
	sed -i 's/Version: 0.0.0-0/Version: ${VERSION}/g' "./${PACKAGE_NAME}/DEBIAN/control" ;\
	cat ./${PACKAGE_NAME}/DEBIAN/control
	@echo "[INFO] Build Deb Package."
	mkdir -p ./dest
	# prepare new installer code
	rm -rf "./dest/${PACKAGE_NAME}_${VERSION}.deb"
	git clone --branch ${tag} https://github.com/ccmagithub/agena.git
	cp -r ./agena/GPU_management_node ./gpu-management/opt/gemini/
	# build new deb
	dpkg-deb -Znone  -b "./${PACKAGE_NAME}" "./dest/${PACKAGE_NAME}_${VERSION}.deb"
	# mv to package directory
	mkdir ./${VERSION}
	mkdir -p ./${VERSION}/img/
	mkdir -p ./${VERSION}/patch/
	cp ./dest/${PACKAGE_NAME}_${VERSION}.deb ./${VERSION}/
	date > ./${VERSION}/readme.txt

install ::
	dpkg -i "./dest/${PACKAGE_NAME}_${VERSION}.deb"
