PORTNAME=	python2-autobahn
DISTVERSION=	19.11.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Real-time framework for Web, Mobile & Internet of Things.
WWW=		https://crossbar.io/autobahn/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-argon2_cffi@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		??/py-pynacl@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-twistedx@${PY_FLAVOR} \
		??/py-txaio@${PY_FLAVOR} \
		??/py-wsaccel@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
