PORTNAME=	jast
DISTVERSION=	17.361ecde
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Just Another Screenshot Tool.
WWW=		https://github.com/mikehacksthings/jast

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-docopt@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
