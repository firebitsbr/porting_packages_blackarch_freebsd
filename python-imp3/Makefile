PORTNAME=	python-imp3
DISTVERSION=	0.1.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Interactive tool for image pre-processing and automated pipeline creation.
WWW=		https://pypi.org/project/imp3/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-opencv@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-streamlit@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
