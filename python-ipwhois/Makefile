PORTNAME=	python-ipwhois
DISTVERSION=	1.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Retrieve and parse whois data for IPv4 and IPv6 addresses.
WWW=		https://pypi.org/project/ipwhois/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-defusedxml@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-ipaddr@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
