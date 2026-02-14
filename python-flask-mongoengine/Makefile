PORTNAME=	python-flask-mongoengine
DISTVERSION=	1.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Flask extension that provides integration with MongoEngine and WTF model forms.
WWW=		https://pypi.org/project/flask-mongoengine/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-blinker@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-mongoengine@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
