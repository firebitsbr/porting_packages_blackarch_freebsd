PORTNAME=	eyewitness
DISTVERSION=	v20230525.1.r207.gc3286fb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Designed to take screenshots of websites, provide some server header info, and identify default credentials if possible.
WWW=		https://github.com/ChrisTruncer/EyeWitness

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/firefox \
		??/geckodriver \
		??/ghost-py \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-easyprocess@${PY_FLAVOR} \
		??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/py-pytesseract@${PY_FLAVOR} \
		??/py-pyvirtualdisplay@${PY_FLAVOR} \
		??/py-rdpy@${PY_FLAVOR} \
		??/py-rsa@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/xorg-server-xvfb \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
