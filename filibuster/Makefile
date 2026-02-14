PORTNAME=	filibuster
DISTVERSION=	167.c54ac80
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Egress filter mapping application with additional functionality.
WWW=		https://github.com/subinacls/Filibuster

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pyliblzma@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
