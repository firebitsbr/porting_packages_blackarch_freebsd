PORTNAME=	python-pyexcel-xlsx
DISTVERSION=	0.6.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A wrapper library to read, manipulate and write data in xlsx and xlsmformat.
WWW=		https://pypi.org/project/pyexcel-xlsx/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-openpyxl@${PY_FLAVOR} \
		??/py-pyexcel-io@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
