PORTNAME=	python-augmentor
DISTVERSION=	0.2.12
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Image augmentation library for Machine Learning.
WWW=		https://pypi.org/project/Augmentor/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-future@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
