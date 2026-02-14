PORTNAME=	buster
DISTVERSION=	92.131437e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find emails of a person and return info associated with them.
WWW=		https://github.com/sham00n/buster

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/cython \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-grequests@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/twint \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
