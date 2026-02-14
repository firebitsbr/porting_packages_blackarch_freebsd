PORTNAME=	ct-exposer
DISTVERSION=	24.71252ac
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An OSINT tool that discovers sub-domains by searching Certificate Transparency logs.
WWW=		https://github.com/chris408/ct-exposer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-gevent@${PY_FLAVOR} \
		??/py-greenlet@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
