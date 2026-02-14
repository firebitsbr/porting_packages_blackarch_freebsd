PORTNAME=	proxybroker2
DISTVERSION=	552.b7f340a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Proxy [Finder | Checker | Server]. HTTP(S) & SOCKS.
WWW=		https://github.com/bluet/proxybroker2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-cachetools@${PY_FLAVOR} \
		??/py-maxminddb@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
