PORTNAME=	python2-tornado
DISTVERSION=	5.1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python web framework and asynchronous networking library, originally developed at FriendFeed.
WWW=		https://pypi.org/project/tornado/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-backports-abc@${PY_FLAVOR} \
		??/py-futures@${PY_FLAVOR} \
		??/py-singledispatch@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
