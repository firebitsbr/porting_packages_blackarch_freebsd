PORTNAME=	python-antlerinator
DISTVERSION=	4.9.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python utility package to help keeping components of ANTLR v4 in sync.
WWW=		https://pypi.org/project/antlerinator/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-antlr4@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
