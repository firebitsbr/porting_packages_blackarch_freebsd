PORTNAME=	python-pyexcel
DISTVERSION=	0.7.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A wrapper library that provides one API to read, manipulate and writedata in different excel formats.
WWW=		https://pypi.org/project/pyexcel/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-lml@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pyexcel-io@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
