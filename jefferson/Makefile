PORTNAME=	jefferson
DISTVERSION=	v0.4.7.r0.g7dde59d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	JFFS2 filesystem extraction tool.
WWW=		https://github.com/onekey-sec/jefferson

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-cstruct@${PY_FLAVOR} \
		??/py-lzallright@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
