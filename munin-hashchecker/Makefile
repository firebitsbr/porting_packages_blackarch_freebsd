PORTNAME=	munin-hashchecker
DISTVERSION=	242.95ac249
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Online hash checker for Virustotal and other services
WWW=		https://github.com/Neo23x0/munin

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cfscrape@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-flask-caching@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-pymisp@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
