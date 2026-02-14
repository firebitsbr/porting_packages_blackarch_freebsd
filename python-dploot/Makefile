PORTNAME=	python-dploot
DISTVERSION=	3.1.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	DPAPI looting remotely.
WWW=		https://github.com/zblurx/dploot

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket-ba \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
