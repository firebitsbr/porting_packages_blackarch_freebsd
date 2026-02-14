PORTNAME=	python-svgutils
DISTVERSION=	0.3.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Create and manipulate SVG files.
WWW=		URL pointing to download section of package

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-numpydoc@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sphinx_rtd_theme@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
