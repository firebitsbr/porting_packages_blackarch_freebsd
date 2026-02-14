PORTNAME=	frida-push
DISTVERSION=	1.0.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Wrapper tool to identify the remote device and push device specific frida-server binary
WWW=		https://github.com/AndroidTamer/frida-push

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-backports-lzma@${PY_FLAVOR} \
		??/py-frida@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
