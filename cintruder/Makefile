PORTNAME=	cintruder
DISTVERSION=	14.f8a3f12
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An automatic pentesting tool to bypass captchas.
WWW=		https://github.com/epsylon/cintruder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
