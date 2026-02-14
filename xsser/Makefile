PORTNAME=	xsser
DISTVERSION=	1.8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A penetration testing tool for detecting and exploiting XSS vulnerabilites.
WWW=		https://xsser.03c8.net/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/orbited \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cairo@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-gobject@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		??/pygtk \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
