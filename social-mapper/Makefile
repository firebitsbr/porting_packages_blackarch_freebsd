PORTNAME=	social-mapper
DISTVERSION=	190.92be8da
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A social media enumeration and correlation tool.
WWW=		https://github.com/SpiderLabs/social_mapper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/cookiejar \
		??/ipython \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-dlib@${PY_FLAVOR} \
		??/py-easyprocess@${PY_FLAVOR} \
		??/py-face-recognition-models@${PY_FLAVOR} \
		??/py-face-recognition@${PY_FLAVOR} \
		??/py-facebook-sdk@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pyvirtualdisplay@${PY_FLAVOR} \
		??/py-scikit-image@${PY_FLAVOR} \
		??/py-scikit-learn@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
