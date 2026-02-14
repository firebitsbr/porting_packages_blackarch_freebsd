PORTNAME=	python-azure-mgmt-storage
DISTVERSION=	24.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Microsoft Azure Storage Management Client Library for Python.
WWW=		https://pypi.org/project/azure-mgmt-storage/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-azure-common@${PY_FLAVOR} \
		??/py-msrest@${PY_FLAVOR} \
		??/py-msrestazure@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
