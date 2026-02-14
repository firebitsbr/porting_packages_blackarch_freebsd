PORTNAME=	loki-scanner
DISTVERSION=	1258.7688421
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple IOC and Incident Response Scanner.
WWW=		https://github.com/Neo23x0/Loki

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-helpers@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-pylzma@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-rfc5424-logging-handler@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-tzlocal@${PY_FLAVOR} \
		??/py-yara@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
