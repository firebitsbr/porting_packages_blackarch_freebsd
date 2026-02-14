PORTNAME=	python-stix2
DISTVERSION=	3.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Produce and consume STIX 2 JSON content.
WWW=		https://github.com/oasis-open/cti-python-stix2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-stix2-patterns@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
