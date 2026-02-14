PORTNAME=	entropy
DISTVERSION=	702.13aac50
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A set of tools to exploit Netwave and GoAhead IP Webcams.
WWW=		https://github.com/entynetproject/entropy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-shodan@${PY_FLAVOR} \
		??/py-tailer@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
