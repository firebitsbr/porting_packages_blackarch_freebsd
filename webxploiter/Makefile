PORTNAME=	webxploiter
DISTVERSION=	56.c03fe6b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An OWASP Top 10 Security scanner.
WWW=		https://github.com/xionsec/WebXploiter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ghost-py \
		??/libffi \
		??/py-ndg-httpsclient@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		security/openssl \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
