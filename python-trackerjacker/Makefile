PORTNAME=	python-trackerjacker
DISTVERSION=	2.0.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Finds and tracks wifi devices through raw 802.11 monitoring.
WWW=		https://github.com/calebmadrigal/trackerjacker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pyaml@${PY_FLAVOR} \
		??/py-ruamel-yaml@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
