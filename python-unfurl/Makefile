PORTNAME=	python-unfurl
DISTVERSION=	2021.06.15
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Use Git to record and deploy changes to your DevOps infrastructure.
WWW=		https://github.com/obsidianforensics/unfurl

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-maclookup@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-protobuf@${PY_FLAVOR} \
		??/py-publicsuffix2@${PY_FLAVOR} \
		??/py-pycountry@${PY_FLAVOR} \
		??/py-torf@${PY_FLAVOR} \
		??/py-ulid-py@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
