PORTNAME=	xsrfprobe
DISTVERSION=	575.b051d78
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Prime Cross Site Request Forgery Audit and Exploitation Toolkit.
WWW=		https://github.com/0xInfection/XSRFProbe

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dos2unix \
		??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-stringdist@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yattag@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
