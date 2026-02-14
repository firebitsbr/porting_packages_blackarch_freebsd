PORTNAME=	gitdump
DISTVERSION=	1.682fa37
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A pentesting tool that dumps the source code from .git even when the directory traversal is disabled.
WWW=		https://github.com/Ebryx/GitDump

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
