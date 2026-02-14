PORTNAME=	mwebfp
DISTVERSION=	16.a800b98
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Mass Web Fingerprinter.
WWW=		https://github.com/falcon-lnhg/mwebfp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/cutycapt \
		??/py-nmap@${PY_FLAVOR} \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
