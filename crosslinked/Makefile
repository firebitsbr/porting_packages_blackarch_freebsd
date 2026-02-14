PORTNAME=	crosslinked
DISTVERSION=	v0.3.0.r23.g2ae8d7b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	LinkedIn enumeration tool to extract valid employee names from an organization through search engine scraping.
WWW=		https://github.com/m8r0wn/crosslinked

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-taser@${PY_FLAVOR} \
		??/py-unidecode@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
