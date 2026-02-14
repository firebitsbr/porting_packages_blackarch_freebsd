PORTNAME=	server-status-pwn
DISTVERSION=	12.841d55d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A script that monitors and extracts requested URLs and clients connected to the service by exploiting publicly accessible Apache server-status instances.
WWW=		https://github.com/mazen160/server-status_PWN

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
