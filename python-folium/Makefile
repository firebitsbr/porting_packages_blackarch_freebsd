PORTNAME=	python-folium
DISTVERSION=	0.20.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Make beautiful maps with Leaflet.js & Python.
WWW=		https://pypi.org/project/folium/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-branca@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-xyzservices@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
