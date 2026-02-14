PORTNAME=	pyrdp
DISTVERSION=	2094.2147093
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python 3 RDP MITM and library.
WWW=		https://github.com/GoSecure/pyrdp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-appdirs@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dbus@${PY_FLAVOR} \
		??/py-names@${PY_FLAVOR} \
		??/py-notify2@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-rsa@${PY_FLAVOR} \
		??/py-service-identity@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
