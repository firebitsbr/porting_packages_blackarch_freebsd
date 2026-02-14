PORTNAME=	python-python-registry
DISTVERSION=	1.3.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Read access to Windows Registry files.
WWW=		https://pypi.org/project/python-registry/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-enum-compat@${PY_FLAVOR} \
		??/py-unicodecsv@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
