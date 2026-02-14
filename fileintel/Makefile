PORTNAME=	fileintel
DISTVERSION=	33.a0bff38
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular Python application to pull intelligence about malicious files.
WWW=		https://github.com/keithjjones/fileintel

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-otxv2@${PY_FLAVOR} \
		??/py-threatcrowd@${PY_FLAVOR} \
		??/py-virustotal-api@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
