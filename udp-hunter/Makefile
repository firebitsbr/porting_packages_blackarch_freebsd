PORTNAME=	udp-hunter
DISTVERSION=	4.b95cce5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network assessment tool for various UDP Services covering both IPv4 and IPv6 protocols.
WWW=		https://github.com/NotSoSecure/udp-hunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-ifaddr@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
