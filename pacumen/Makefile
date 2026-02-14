PORTNAME=	pacumen
DISTVERSION=	1.92a0884
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Packet Acumen - Analyse encrypted network traffic and more (side-channel attacks).
WWW=		https://github.com/bniemczyk/pacumen

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-numpy@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-symath@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
