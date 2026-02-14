PORTNAME=	pygpoabuse
DISTVERSION=	36.324a3c3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	RCE via GPO scheduled tasks.
WWW=		https://github.com/Hackndo/pyGPOAbuse

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-msldap@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
