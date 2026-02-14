PORTNAME=	python-dissect.cim
DISTVERSION=	3.13.r0.g5642f99
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Dissect module implementing a parser for the Windows Common Information Model (CIM) database, used in the Windows operating system.
WWW=		https://github.com/fox-it/dissect.cim

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
