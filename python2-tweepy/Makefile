PORTNAME=	python2-tweepy
DISTVERSION=	3.8.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python library for accessing the entire Twitter API.
WWW=		https://pypi.org/project/tweepy/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-requests-oauthlib@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}

RUN_DEPENDS=	??/py-pysocks@${PY_FLAVOR} \
		??/py-requests-oauthlib@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
