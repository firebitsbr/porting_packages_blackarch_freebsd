PORTNAME=	python2-shiboken
DISTVERSION=	1.2.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	
WWW=		https://github.com/pyside/Shiboken/tags

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/py-distutils-extra@${PY_FLAVOR} \
		??/qt4 \
		lang/python \
		lang/python3 \
		security/openssl \
		textproc/libxslt

RUN_DEPENDS=	??/libicu64


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
