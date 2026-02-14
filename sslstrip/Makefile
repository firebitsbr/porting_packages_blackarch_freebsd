PORTNAME=	sslstrip
DISTVERSION=	0.9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python tool to hijack HTTPS connections during a MITM attack.
WWW=		https://github.com/moxie0/sslstrip

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-pyopenssl@${PY_FLAVOR} \
		??/py-service-identity@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
