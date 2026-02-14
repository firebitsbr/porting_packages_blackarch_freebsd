PORTNAME=	reconscan
DISTVERSION=	61.afbcfc0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network reconnaissance and vulnerability assessment tools.
WWW=		https://github.com/RoliSoft/ReconScan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
