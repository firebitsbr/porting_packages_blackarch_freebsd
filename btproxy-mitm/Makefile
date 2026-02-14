PORTNAME=	btproxy-mitm
DISTVERSION=	71.cd1c906
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Man in the Middle analysis tool for Bluetooth.
WWW=		https://github.com/conorpp/btproxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/bluez-libs \
		??/gcc \
		??/py-dbus@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
