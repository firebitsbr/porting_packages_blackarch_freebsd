PORTNAME=	h2csmuggler
DISTVERSION=	7.7ea573a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	HTTP Request Smuggling over HTTP/2 Cleartext (h2c).
WWW=		https://github.com/BishopFox/h2csmuggler

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-h2@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
