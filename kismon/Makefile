PORTNAME=	kismon
DISTVERSION=	1.0.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	GUI client for kismet (wireless scanner/sniffer/monitor).
WWW=		https://www.salecker.org/software/kismon.html

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/gobject-introspection-runtime \
		??/gtk3 \
		??/kismet \
		??/osm-gps-map \
		??/py-cairo@${PY_FLAVOR} \
		??/py-gobject@${PY_FLAVOR} \
		??/py-kismet-rest@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
