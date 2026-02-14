PORTNAME=	termineter
DISTVERSION=	210.a802f94
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Smart meter testing framework.
WWW=		https://code.google.com/p/termineter/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-crcelk@${PY_FLAVOR} \
		??/py-pluginbase@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		??/py-smoke-zephyr@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
