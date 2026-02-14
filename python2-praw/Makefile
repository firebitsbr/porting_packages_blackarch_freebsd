PORTNAME=	python2-praw
DISTVERSION=	6.4.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python Reddit API Wrapper that allows for simple access to reddits API.
WWW=		https://praw.readthedocs.org

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pytest-runner@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-prawcore@${PY_FLAVOR} \
		??/py-update-checker@${PY_FLAVOR} \
		??/py-websocket-client@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
