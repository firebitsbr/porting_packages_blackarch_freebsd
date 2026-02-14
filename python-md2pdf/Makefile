PORTNAME=	python-md2pdf
DISTVERSION=	3.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python-based Markdown to PDF converter.
WWW=		https://pypi.org/project/md2pdf

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-docopt@${PY_FLAVOR} \
		??/py-markdown2@${PY_FLAVOR} \
		??/py-weasyprint@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
