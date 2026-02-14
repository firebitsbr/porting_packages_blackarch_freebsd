PORTNAME=	pytbull
DISTVERSION=	19.3d82a54
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Next generation of pytbull, IDS/IPS testing framework.
WWW=		https://github.com/netrunn3r/pytbull-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cherrypy@${PY_FLAVOR} \
		??/py-feedparser@${PY_FLAVOR} \
		??/py-m2crypto@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
