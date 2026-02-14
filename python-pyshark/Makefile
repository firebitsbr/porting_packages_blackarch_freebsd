PORTNAME=	python-pyshark
DISTVERSION=	0.6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python wrapper for tshark, allowing python packet parsing using wireshark dissectors.
WWW=		https://pypi.org/project/pyshark/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-logbook@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
