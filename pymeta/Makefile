PORTNAME=	pymeta
DISTVERSION=	1.0.4.r25.gdb8a80b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Auto Scanning to SSL Vulnerability.
WWW=		https://github.com/m8r0wn/pymeta

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/perl-image-exiftool \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
