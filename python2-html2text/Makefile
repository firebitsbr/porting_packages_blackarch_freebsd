PORTNAME=	python2-html2text
DISTVERSION=	2019.8.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Turn HTML into equivalent Markdown-structured text.
WWW=		https://pypi.org/project/html2text/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-coverage@${PY_FLAVOR} \
		??/py-tox@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
