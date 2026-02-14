PORTNAME=	corscanner
DISTVERSION=	1.0.1.r2.g593043f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fast CORS misconfiguration vulnerabilities scanner.
WWW=		https://github.com/chenjj/CORScanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-requests-file@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
