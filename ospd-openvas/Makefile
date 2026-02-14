PORTNAME=	ospd-openvas
DISTVERSION=	22.7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An OSP server implementation to allow GVM to remotely control an OpenVAS Scanner.
WWW=		https://github.com/greenbone/ospd-openvas

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	??/openvas-scanner \
		??/py-defusedxml@${PY_FLAVOR} \
		??/py-deprecated@${PY_FLAVOR} \
		??/py-gnupg@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-paho-mqtt@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
