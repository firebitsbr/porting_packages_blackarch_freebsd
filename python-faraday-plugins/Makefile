PORTNAME=	python-faraday-plugins
DISTVERSION=	1.27.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Faraday plugins package.
WWW=		https://pypi.org/project/faraday-plugins/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-html2text@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
