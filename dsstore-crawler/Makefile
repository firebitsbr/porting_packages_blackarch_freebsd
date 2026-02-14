PORTNAME=	dsstore-crawler
DISTVERSION=	7.efa51f5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A parser + crawler for .DS_Store files exposed publically.
WWW=		https://github.com/anantshri/DS_Store_crawler_parser

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ds-store@${PY_FLAVOR} \
		??/py-mac-alias@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
