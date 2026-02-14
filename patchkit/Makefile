PORTNAME=	patchkit
DISTVERSION=	37.95dc699
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Powerful binary patching from Python.
WWW=		https://github.com/lunixbochs/patchkit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-coding@${PY_FLAVOR} \
		??/py-keystone@${PY_FLAVOR} \
		??/unicorn \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
