PORTNAME=	python-pyvis
DISTVERSION=	0.3.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python network visualization library.
WWW=		https://pypi.org/project/pyvis/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/ipython \
		??/py-jinja@${PY_FLAVOR} \
		??/py-jsonpickle@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
