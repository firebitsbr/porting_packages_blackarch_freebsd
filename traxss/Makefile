PORTNAME=	traxss
DISTVERSION=	81.48dee2e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated XSS Vulnerability Scanner.
WWW=		https://github.com/M4cs/traxss

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-crayons@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
