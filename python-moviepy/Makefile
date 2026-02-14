PORTNAME=	python-moviepy
DISTVERSION=	2.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Video editing with Python
WWW=		https://pypi.org/project/moviepy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-decorator@${PY_FLAVOR} \
		??/py-dotenv@${PY_FLAVOR} \
		??/py-imageio-ffmpeg@${PY_FLAVOR} \
		??/py-imageio@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-proglog@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
