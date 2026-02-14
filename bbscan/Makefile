PORTNAME=	bbscan
DISTVERSION=	53.29b9f11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tiny Batch web vulnerability Scanner.
WWW=		https://github.com/lijiejie/bbscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
