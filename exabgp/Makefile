PORTNAME=	exabgp
DISTVERSION=	4.0.2.r2397.gebdbdd5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The BGP swiss army knife of networking.
WWW=		https://github.com/Exa-Networks/exabgp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-ipaddr@${PY_FLAVOR} \
		??/py-nose@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
