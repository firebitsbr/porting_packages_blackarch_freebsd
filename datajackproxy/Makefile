PORTNAME=	datajackproxy
DISTVERSION=	42.f75f3a3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A proxy which allows you to intercept TLS traffic in native x86 applications across platform.
WWW=		https://github.com/nccgroup/DatajackProxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-frida@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
