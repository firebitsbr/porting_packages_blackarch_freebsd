PORTNAME=	pagodo
DISTVERSION=	163.33c4c0f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google dork script to collect potentially vulnerable web pages and applications on the Internet.
WWW=		https://github.com/opsdisk/pagodo

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-google@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-yagooglesearch@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
