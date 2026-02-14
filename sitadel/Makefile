PORTNAME=	sitadel
DISTVERSION=	123.e4d9ed4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Web Application Security Scanner.
WWW=		https://github.com/shenril/Sitadel

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/scrapy \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
