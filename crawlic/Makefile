PORTNAME=	crawlic
DISTVERSION=	51.739fe2b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Web recon tool (find temporary files, parse robots.txt, search folders, google dorks and search domains hosted on same server).
WWW=		https://github.com/Ganapati/Crawlic

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-simplejson@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
