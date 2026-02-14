PORTNAME=	python-enaml
DISTVERSION=	0.19.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Declarative DSL for building rich user interfaces in Python.
WWW=		https://pypi.org/project/enaml/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-atom@${PY_FLAVOR} \
		??/py-kiwisolver@${PY_FLAVOR} \
		??/py-ply@${PY_FLAVOR} \
		??/py-qtpy@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
