PORTNAME=	dnsvalidator
DISTVERSION=	82.146c9b0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Maintains a list of IPv4 DNS servers by verifying them against baseline servers, and ensuring accurate responses.
WWW=		https://github.com/vortexau/dnsvalidator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorclass@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
