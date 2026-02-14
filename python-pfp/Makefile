PORTNAME=	python-pfp
DISTVERSION=	0.4.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An interpreter for 010 template scripts.
WWW=		https://github.com/d0c-s4vage/pfp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-intervaltree@${PY_FLAVOR} \
		??/py-py010parser@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
