PORTNAME=	cantoolz
DISTVERSION=	425.82d330b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Framework for black-box CAN network analysis.
WWW=		https://github.com/CANToolz/CANToolz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-bitstring@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-mido@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
