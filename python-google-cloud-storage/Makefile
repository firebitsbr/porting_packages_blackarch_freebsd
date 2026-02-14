PORTNAME=	python-google-cloud-storage
DISTVERSION=	3.9.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Google Cloud Storage API client library.
WWW=		https://pypi.org/project/google-cloud-storage/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-google-api-core@${PY_FLAVOR} \
		??/py-google-auth@${PY_FLAVOR} \
		??/py-google-cloud-core@${PY_FLAVOR} \
		??/py-google-crc32c@${PY_FLAVOR} \
		??/py-google-resumable-media@${PY_FLAVOR} \
		??/py-protobuf@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
