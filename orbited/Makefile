PORTNAME=	orbited
DISTVERSION=	0.7.10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A browser(javascript)->tcp bridge; Comet is used to emulate TCP connections in the browser; Allows you to connect a web browser directly to an IRC or XMPP server, for instance.
WWW=		https://pypi.org/project/orbited/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/morbid \
		??/py-demjson@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		??/stomper \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
