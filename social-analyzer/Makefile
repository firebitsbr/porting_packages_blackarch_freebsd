PORTNAME=	social-analyzer
DISTVERSION=	0.45
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Analyzing & finding a persons profile across social media websites.
WWW=		https://pypi.org/project/social-analyzer/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-galeodes@${PY_FLAVOR} \
		??/py-langdetect@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
