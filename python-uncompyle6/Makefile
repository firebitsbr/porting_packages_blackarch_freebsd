PORTNAME=	python-uncompyle6
DISTVERSION=	3.9.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python cross-version decompiler.
WWW=		https://pypi.org/project/uncompyle6/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-hypothesis@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-spark-parser@${PY_FLAVOR} \
		??/py-xdis@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
