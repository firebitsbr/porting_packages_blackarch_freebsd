PORTNAME=	ghidriff
DISTVERSION=	v1.0.0.r2.g53e16cf
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python Command-Line Ghidra Binary Diffing Engine.
WWW=		https://github.com/clearbluejar/ghidriff

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-mdutils@${PY_FLAVOR} \
		??/py-pyghidra@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
