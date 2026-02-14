PORTNAME=	python-xhtml2pdf
DISTVERSION=	0.2.17
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	PDF generator using HTML and CSS.
WWW=		https://pypi.org/project/xhtml2pdf/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-arabic-reshaper@${PY_FLAVOR} \
		??/py-bidi@${PY_FLAVOR} \
		??/py-html5lib@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pypdf2@${PY_FLAVOR} \
		??/py-reportlab@${PY_FLAVOR} \
		??/py-svglib@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
