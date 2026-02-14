PORTNAME=	pex
DISTVERSION=	617.0a776da
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A collection of special tools for providing high quality penetration testing.
WWW=		https://pypi.org/project/pex/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-alive-progress@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
