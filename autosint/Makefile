PORTNAME=	autosint
DISTVERSION=	236.25d292c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to automate common osint tasks.
WWW=		https://github.com/bharshbarger/AutOSINT

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-docx@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
