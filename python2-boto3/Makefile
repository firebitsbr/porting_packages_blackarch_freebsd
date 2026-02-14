PORTNAME=	python2-boto3
DISTVERSION=	1.10.19
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The AWS SDK for Python.
WWW=		https://pypi.org/project/boto3/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-botocore@${PY_FLAVOR} \
		??/py-jmespath@${PY_FLAVOR} \
		??/py-s3transfer@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
