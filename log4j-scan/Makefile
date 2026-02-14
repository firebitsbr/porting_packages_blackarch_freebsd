PORTNAME=	log4j-scan
DISTVERSION=	88.07f7e32
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A fully automated, accurate, and extensive scanner for finding log4j RCE CVE-2021-44228.
WWW=		https://github.com/fullhunt/log4j-scan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pycryptodome@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
