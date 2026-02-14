PORTNAME=	dnsrecon
DISTVERSION=	1.5.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python script for enumeration of hosts, subdomains and emails from a given domain using google.
WWW=		https://github.com/darkoperator/dnsrecon

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-loguru@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
