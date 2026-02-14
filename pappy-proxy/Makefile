PORTNAME=	pappy-proxy
DISTVERSION=	77.e1bb049
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An intercepting proxy for web application testing.
WWW=		https://github.com/roglew/pappy-proxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-apsw@${PY_FLAVOR} \
		??/py-autobahn@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cmd2@${PY_FLAVOR} \
		??/py-crochet@${PY_FLAVOR} \
		??/py-decorator@${PY_FLAVOR} \
		??/py-j2cli@${PY_FLAVOR} \
		??/py-mock@${PY_FLAVOR} \
		??/py-parsley@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		??/py-pytest-cov@${PY_FLAVOR} \
		??/py-pytest-mock@${PY_FLAVOR} \
		??/py-pytest-twisted@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-scrypt@${PY_FLAVOR} \
		??/py-service-identity@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		??/py-txsocksx@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
