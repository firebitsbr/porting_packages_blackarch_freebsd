PORTNAME=	secretfinder
DISTVERSION=	15.d06119d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python script to find sensitive data (apikeys, accesstoken, jwt,..) in javascript files.
WWW=		https://github.com/m4ll0k/SecretFinder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-jsbeautifier@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
