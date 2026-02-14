PORTNAME=	iptv
DISTVERSION=	138.ae6457b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Search and brute force illegal iptv server.
WWW=		https://github.com/Pinperepette/IPTV

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-clint@${PY_FLAVOR} \
		??/py-colored@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pyprind@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
