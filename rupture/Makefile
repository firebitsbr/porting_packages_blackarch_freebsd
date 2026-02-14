PORTNAME=	rupture
DISTVERSION=	1383.131c61a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A framework for BREACH and other compression-based crypto attacks.
WWW=		https://github.com/decrypto-org/rupture

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bettercap \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-coverage@${PY_FLAVOR} \
		??/py-coveralls@${PY_FLAVOR} \
		??/py-django-nose@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pycodestyle@${PY_FLAVOR} \
		??/py-tlslite-ng@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/scapy \
		lang/python3 \
		shells/bash \
		www/npm \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
