PORTNAME=	python-hammertime-http
DISTVERSION=	0.11.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An HTTP client library aiming to perform a large number of requests on a server as fast as it can take them, but without distrupting operations significantly.
WWW=		https://pypi.org/project/HammerTime-http/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-easyinject@${PY_FLAVOR} \
		??/py-marshmallow-autoschema@${PY_FLAVOR} \
		??/py-marshmallow-har@${PY_FLAVOR} \
		??/py-simhash@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
