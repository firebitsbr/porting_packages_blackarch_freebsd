PORTNAME=	dnsgen
DISTVERSION=	v1.0.4.r12.g7c98e7e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate combination of domain names from the provided input.
WWW=		https://github.com/AlephNullSK/dnsgen

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
