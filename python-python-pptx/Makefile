PORTNAME=	python-python-pptx
DISTVERSION=	1.0.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generate and manipulate Open XML PowerPoint (.pptx) files.
WWW=		https://pypi.org/project/python-pptx/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
