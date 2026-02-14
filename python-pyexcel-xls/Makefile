PORTNAME=	python-pyexcel-xls
DISTVERSION=	0.7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A wrapper library to read, manipulate and write data in xls format. It reads xlsx and xlsm format.
WWW=		https://pypi.org/project/pyexcel-xls/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pyexcel-io@${PY_FLAVOR} \
		??/py-xlrd@${PY_FLAVOR} \
		??/py-xlwt@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
