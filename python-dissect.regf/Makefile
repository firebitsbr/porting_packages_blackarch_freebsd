PORTNAME=	python-dissect.regf
DISTVERSION=	3.14.r0.gc0fc829
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Dissect module implementing a parser for Windows registry file format, used to store application and OS configuration on Windows operating systems.
WWW=		https://github.com/fox-it/dissect.regf

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dissect.cstruct@${PY_FLAVOR} \
		??/py-dissect.util@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
