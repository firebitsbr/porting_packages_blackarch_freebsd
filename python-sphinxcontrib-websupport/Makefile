PORTNAME=	python-sphinxcontrib-websupport
DISTVERSION=	2.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Sphinx API for Web Apps
WWW=		https://pypi.org/project/sphinxcontrib-websupport/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-flit-core@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-jinja@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sphinxcontrib-serializinghtml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
