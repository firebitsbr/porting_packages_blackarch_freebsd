PORTNAME=	python-lsassy
DISTVERSION=	v3.1.14.r3.g78c0c59
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python library to remotely extract credentials on a set of hosts.
WWW=		https://github.com/Hackndo/lsassy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pypykatz@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
