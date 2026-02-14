PORTNAME=	amoco
DISTVERSION=	v2.9.11.r4.g3e36c52
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Yet another tool for analysing binaries.
WWW=		https://github.com/bdcht/amoco

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-blessed@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-crysp@${PY_FLAVOR} \
		??/py-grandalf@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-traitlets@${PY_FLAVOR} \
		??/py-z3-solver@${PY_FLAVOR} \
		??/pygoocanvas \
		??/pygtk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
