PORTNAME=	jsparser
DISTVERSION=	31.ccd3ab6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Parse javascript using Tornado and JSBeautifier to discover interesting enpoints.
WWW=		https://github.com/nahamsec/JSParser

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-jsbeautifier@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-safeurl@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
