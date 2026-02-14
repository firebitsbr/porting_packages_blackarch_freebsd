PORTNAME=	netscan2
DISTVERSION=	60.3d02ba1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Active / passive network scanner.
WWW=		https://github.com/walchko/netscan2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build-utils@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mitmproxy \
		??/py-awake@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
