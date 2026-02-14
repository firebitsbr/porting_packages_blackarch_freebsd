PORTNAME=	sublert
DISTVERSION=	67.56d2a12
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A security and reconnaissance tool which leverages certificate transparency to automatically monitor new subdomains deployed by specific organizations and issued TLS/SSL certificate.
WWW=		https://github.com/yassineaboukir/sublert

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
