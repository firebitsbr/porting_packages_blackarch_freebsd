PORTNAME=	nsec3map
DISTVERSION=	v0.8.2.r0.gd145b13
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to enumerate the resource records of a DNS zone using its DNSSEC NSEC or NSEC3 chain.
WWW=		https://github.com/anonion0/nsec3map

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		lang/python \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
