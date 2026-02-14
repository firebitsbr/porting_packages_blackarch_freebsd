PORTNAME=	python-flickrapi
DISTVERSION=	2.4.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The official Python interface to the Flickr API.
WWW=		https://stuvel.eu/flickrapi

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-requests-oauthlib@${PY_FLAVOR} \
		??/py-requests-toolbelt@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
