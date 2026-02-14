PORTNAME=	metafinder
DISTVERSION=	v1.2.r2.g30c8475
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Search for documents in a domain through Search Engines (Google, Bing and Baidu). The objective is to extract metadata.
WWW=		https://github.com/Josue87/MetaFinder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-docx@${PY_FLAVOR} \
		??/py-openpyxl@${PY_FLAVOR} \
		??/py-pikepdf@${PY_FLAVOR} \
		??/py-pptx@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
