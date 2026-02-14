PORTNAME=	honeypy
DISTVERSION=	600.6ca3d6e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A low interaction Honeypot.
WWW=		https://github.com/foospidy/HoneyPy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
